from manim import *
import math, itertools, functools, random

def gen_binom(n, k):
    coeff = 1
    if n < 0 and k < 0:
        return(0)
    for j in range(0, k):
        coeff = coeff * (n - j) / (j + 1)
    return(coeff)
        

def int_binom(n: int, k: int) -> int:
        return(int(gen_binom(n, k)))

def itr_interleave(*iterables):
    unfiltered = itertools.chain.from_iterable(itertools.zip_longest(*iterables))
    return(filter(lambda i: i is not None, unfiltered))

def centroid(*iterables):
    sum = functools.reduce((lambda x,y: x + y), iterables)
    return(sum / float(len(iterables)))

def center_centroid(*iterables):
    return(centroid(*map((lambda x : x.get_center()), iterables)))

class PascalTriangle(Scene):
    def construct(self):
        coeff = [[int_binom(i, j) for j in range(0, i + 1)] for i in range(0, 4)]
        tex_wrap = (lambda x: MathTex(str(x)))
        triangle = VGroup(*[VGroup(*map(tex_wrap, coeff[i])).arrange_submobjects(RIGHT, buff = 2) for i in range(len(coeff))]).arrange_submobjects(DOWN, buff = 2)
        
        self.play(Write(triangle), run_time=6)
        self.wait(3)

class SumAnimation(Scene):
    def construct(self):
        # There's a great historical angle on this: https://youtu.be/gMlf1ELvRzc?t=398
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

class SubsetSelection(Scene):
    def construct(self):
        # Universal Set creation:
        U_circle = Circle(color = WHITE, radius = 3.0)
        U_label = MathTex("\mathbb{U}")
        U_label.next_to(U_circle, direction=UP)
        universal_set = VGroup(U_circle, U_label)

        # Member Creation:
        members = VGroup(*map((lambda c: Dot(color = c, radius = 0.15)), [RED, BLUE, GREEN, YELLOW, PURPLE]))
        for dot in members.submobjects:
            dot.shift(random.random() * 4.5 * UP + random.random() * 4.5 * LEFT - 2.25 * UP - 2.25 * LEFT)
            #members.rotate_about_origin(random.random() * 2 * math.pi / float(len(members)))
        
        # Subset Creation:
        S1_circle = Circle(color = WHITE, radius = 0.7)
        S1_circle.shift(0.3 * LEFT + DOWN)
        S2_circle = Circle(color = WHITE, radius = 1.0)
        S2_circle.shift(1.5 * LEFT)

        subset_circles = [S1_circle, S2_circle]

        self.play(FadeIn(universal_set), FadeIn(members))
        # "Say you wanted to pick a set of 2 objects from another set U"
        self.wait(3)
        self.play(ShowCreation(subset_circles[0]))
        # "Here's one example of such a set."
        self.wait(3)
        # "Of course, it's not the only one we can make."
        self.play(Uncreate(subset_circles[0]))
        self.play(ShowCreation(subset_circles[1]))
        self.wait(3)

class Polynomial_Mult(Scene):
    def construct(self):
        row_prev = self.row_gen(3, buff = 0.6)
        row_prev.shift(1.5 * UP)
        self.play(Write(row_prev))
        self.wait(3)
        mult_sign = MathTex("\\times")
        mult_sign.shift(4.0 * LEFT)
        prod_line = Line(4.5 * LEFT, 4.5 * RIGHT)
        prod_line.shift(0.5 * DOWN)
        binom_factor = self.row_gen(1, dir = LEFT, buff = 0.6)
        binom_factor.shift(1.93 * RIGHT)
        self.play(Write(binom_factor), Write(mult_sign), Write(prod_line))
    
    def row_gen(self, n, dir = RIGHT, buff = 1, show_all = False):
        coeff_data = [(int_binom(n, i), i) for i in range(0, n + 1)]
        
        def tex_monomial(x):
            if show_all:
                return(MathTex(str(x[0]), 'x^' + str(x[1])))
            else:
                if x[1] == 0:
                    return(MathTex(str(x[0])))
                else:
                    coeff = ""
                    if not x[0] == 1:
                        coeff = str(x[0])
                    if x[1] == 1:
                        return(MathTex(coeff, 'x'))
                    else:
                        return(MathTex(coeff, 'x^' + str(x[1])))
                
        monomials_tex = map(tex_monomial, coeff_data)
        plusses = [MathTex("+") for i in range(0, n)]
        polynomial_tex = VGroup(*itr_interleave(monomials_tex, plusses)).arrange_submobjects(dir, buff = buff)
        return(polynomial_tex)
