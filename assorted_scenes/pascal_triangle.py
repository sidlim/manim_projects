from manim import *
import math, itertools, functools

def int_binom(n: int, k: int) -> int:
    if (k < 0) or (k > n):
        return(0)
    else:
        return(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))    

def centroid(*iterables):
    sum = functools.reduce((lambda x,y: x + y), iterables)
    return(sum / float(len(iterables)))

def center_centroid(*iterables):
    return(centroid(*map((lambda x : x.get_center()), iterables)))

class VRow(VGroup):
    def __init__(self, *vmobjects, spacing = 1 * RIGHT, **kwargs):
        super().__init__(**kwargs)
        vmobj_ct = len(vmobjects)
        center_offset = ((vmobj_ct - 1) % 2) / 2.0 * spacing
        spacing_offset = (((vmobj_ct - 1) // 2) - vmobj_ct + 1) * spacing
        for vmobj in vmobjects:
            self.add(vmobj)
            vmobj.shift(center_offset + spacing_offset)
            spacing_offset += spacing

class PascalTriangle(Scene):
    def construct(self):
        coeff = [[int_binom(i, j) for j in range(0, i + 1)] for i in range(0, 4)]
        tex_wrap = (lambda x: MathTex(str(x)))
        triangle = VRow(*[VRow(*map(tex_wrap, coeff[i]), spacing = 2 * RIGHT) for i in range(len(coeff))], spacing = 2 * DOWN)
        #row0 = VRow(*[MathTex(str(int_binom(0, k))) for k in range(0, 1)], spacing = 2 * RIGHT)
        #row1 = VRow(*[MathTex(str(int_binom(1, k))) for k in range(0, 2)], spacing = 2 * RIGHT)
        #row2 = VRow(*[MathTex(str(int_binom(2, k))) for k in range(0, 3)], spacing = 2 * RIGHT)
        #row3 = VRow(*[MathTex(str(int_binom(3, k))) for k in range(0, 4)], spacing = 2 * RIGHT)
        #triangle = VRow(*[row0, row1, row2, row3], spacing = 2 * DOWN)
        self.play(Write(triangle), run_time=6)
        self.wait(3)

class SumAnimation(Scene):
    def construct(self):
        # Build Pascal's Triangle:
        tex_wrap = (lambda x: MathTex(str(x)))
        tex_coeff = {i: {j: tex_wrap(int_binom(i, j)) for j in range(0, i + 1)} for i in range(1, 5)}
        rows = [VGroup(*tex_coeff[i].values()).arrange_submobjects(RIGHT, buff = 2) for i in tex_coeff.keys()]
        triangle = VGroup(*rows).arrange_submobjects(DOWN, buff = 2)        
        for i in tex_coeff.keys():
            self.play(Write(tex_coeff[i][0]), Write(tex_coeff[i][i]))
        self.wait(1)
        for i in itertools.islice(tex_coeff.keys(), 1, None):
            add_rig = self.build_addition_rig(tex_coeff[i - 1][0], tex_coeff[i - 1][1])
            self.wait(1)
            self.play(FadeIn(add_rig), Write(tex_coeff[i][1]))
            for j in range(1, i - 1):
                self.play(add_rig.animate.shift(center_centroid(tex_coeff[i-1][j], tex_coeff[i-1][j+1]) - add_rig.submobjects[0].get_center()))
                self.play(Write(tex_coeff[i][j + 1]))
            self.play(FadeOut(add_rig))

    def build_addition_rig(self, left_el, right_el):
        plus = MathTex("+")
        plus.move_to((left_el.get_center() + right_el.get_center()) / 2.0)
        arrow = Arrow(start = 0.75 * UP, end = 0.75 * DOWN)
        arrow.next_to(plus, DOWN * 1.5)
        add_rig = VGroup(*[plus, arrow])
        return(add_rig)

class PascalMonomials(Scene):
    def construct(self):
        coeff_data = [(int_binom(4, i), i) for i in range(0, 5)]
        tex_wrap = (lambda x: MathTex(str(x[0]), 'x^' + str(x[1])))
        poly = VRow(*map(tex_wrap, coeff_data), spacing = 2 * RIGHT)
        self.play(Write(poly))
        self.wait(6)