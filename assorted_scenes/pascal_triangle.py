from manim import *
import math

def int_binom(n: int, k: int) -> int:
    if (k < 0) or (k > n):
        return(0)
    else:
        return(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))    

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
        coeff = [[int_binom(i, j) for j in range(0, i + 1)] for i in range(0, 4)]
        tex_wrap = (lambda x: MathTex(str(x)))
        rows = [VRow(*map(tex_wrap, coeff[i]), spacing = 2 * RIGHT) for i in range(len(coeff))]

        # triangle is never rendered, but the code helps position its contents appropriately, so I'll keep it
        triangle = VRow(*rows, spacing = 2 * DOWN)
        self.play(Write(rows[0]))

class PascalMonomials(Scene):
    def construct(self):
        coeff_data = [(int_binom(4, i), i) for i in range(0, 5)]
        tex_wrap = (lambda x: MathTex(str(x[0]), 'x^' + str(x[1])))
        poly = VRow(*map(tex_wrap, coeff_data), spacing = 2 * RIGHT)
        self.play(Write(poly))
        self.wait(6)