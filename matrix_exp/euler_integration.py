from manim import *
import math, itertools, functools, random, numpy, logging

# Want a nice visualization of euler integration here
# Table of contents:
# 1 - motivation: 4 moving parts to the DE, complexity
# 2 - 1D case
# 3 - 2D case

class Euler_Integration_2D(Scene):
    def __init__(self, derivative, init_val, dt, n_step, **kwargs):
        super(Euler_Integration_2D, self).__init__(**kwargs)
        self.derivative = derivative
        self.init_val = init_val
        self.dt = dt
        self.n_step = n_step
    
    def construct(self):
        vec_field = VectorField(self.derivative)
        self.add(vec_field)

        x_n = self.init_val

        x_pt = Dot()
        x_pt.move_to(x_n)
        x_pt_label = MathTex("x_" + str(0)).next_to(x_pt, direction = DOWN)
        self.play(FadeIn(x_pt), FadeIn(x_pt_label))
        self.wait(2)

        for n in range(self.n_step):

            Dx = numpy.append(self.derivative(x_n), 0.0)
            Dx_vec = Vector(Dx).put_start_and_end_on(x_n, x_n + Dx)
            Dx_vec_label_pre = MathTex("\\frac{dx}{dt}").next_to(Dx_vec, direction = DOWN)
            Dx_vec_label_post = MathTex("\\frac{1}{" + str(int(1 / self.dt)) + "}\\frac{dx}{dt}").next_to(Dx_vec, direction = DOWN)
            if self.dt == 1:
                Dx_vec_label_post = MathTex("\\frac{dx}{dt}").next_to(Dx_vec, direction = DOWN)
            self.play(FadeIn(Dx_vec), FadeIn(Dx_vec_label_pre))
            self.wait(2)
            self.play(Dx_vec.animate.scale(self.dt, about_point = Dx_vec.get_start()), ReplacementTransform(Dx_vec_label_pre, Dx_vec_label_post))
            self.wait(2)

            x_pt = Dot()
            x_pt.move_to(x_n + self.dt * Dx)
            x_pt_label = MathTex("x_" + str(n + 1)).next_to(x_pt, direction = DOWN)
            self.play(FadeIn(x_pt))
            self.wait(2)

            self.play(FadeOut(Dx_vec), FadeOut(Dx_vec_label_post), FadeIn(x_pt_label))
            self.wait(2)

            x_n = x_n + self.dt * Dx

class Linear_2D_2Step_Int(Euler_Integration_2D):
    def __init__(self):
        A = numpy.array([[0.0, -1.0], [1.0, 0.0]])
        Ax = lambda p: numpy.matmul(A, p[0:2])
        x0 = numpy.array([1.5, 2.0, 0.0])
        super(Linear_2D_2Step_Int, self).__init__(Ax, x0, 0.5, 2)

class Linear_2D_1Step_Int(Euler_Integration_2D):
    def __init__(self):
        A = numpy.array([[0.0, -1.0], [1.0, 0.0]])
        Ax = lambda p: numpy.matmul(A, p[0:2])
        x0 = numpy.array([1.5, 2.0, 0.0])
        super(Linear_2D_1Step_Int, self).__init__(Ax, x0, 1, 1)

class Linear_2D_4Step_Int(Euler_Integration_2D):
    def __init__(self):
        A = numpy.array([[0.0, -1.0], [1.0, 0.0]])
        Ax = lambda p: numpy.matmul(A, p[0:2])
        x0 = numpy.array([1.5, 2.0, 0.0])
        super(Linear_2D_4Step_Int, self).__init__(Ax, x0, 0.25, 4)
