from manim import *
import math, itertools, functools, random, numpy, logging

# Note to self: The only way to make this work is if you modularize it

# First thing to do: Write the animation for stepping a vector along a
# vector field by as much as needed (t, t/2, whatever)

# What that's going to look like:
# Vector field Ax, point x on the vector field
# draw Ax & then show rescale animation by t or t/2
# Show sum as a new point

class Euler_Integration_2D(Scene):
    def __init__(self, derivative, init_val, dt, n_step, **kwargs):
        super(Euler_Integration_2D, self).__init__(**kwargs)
        self.derivative = derivative
        self.init_val = init_val
        self.dt = dt
        self.n_step = n_step
    
    def construct(self):
        vec_field = VectorField(self.derivative)
        x_n = self.init_val
        for n in range(self.n_step):

            x_pt = Dot(point = x_n)
            x_pt_label = MathTex("x_" + str(n)).next_to(x_pt, direction = DOWN)
            self.play(FadeIn(x_pt), FadeIn(x_pt_label))
            self.wait(2)

            Dx = vec_field.get_vector(x_n)
            Dx_vec = Vector(Dx).put_start_and_end_on(x_n, x_n + Dx)
            Dx_vec_label = MathTex("\\frac{dx}{dt}").next_to(Dx_vec, direction = DOWN)
            self.play(FadeIn(Dx_vec), FadeIn(Dx_vec_label))
            self.wait(2)
            self.play(Dx_vec.animate.scale(self.dt))
            
        

# Second thing to do: Write animation for the algebraic expression
# Highlight elements of the line as we go:
# start with just x_{n+1}=x_n
# then add the + Ax_n
# then add the scale (t, t/2, whatever)

# The above is the linear approximation sequence
# Do it twice for the n=2 case and show that there's less error

# Factor, generalize, then limit case

# Discussion: What you can think of e^x as *being* is <mechanistic explanation of Bernoulli Limit>

# the argument here is that the Bernoulli limit is a better intuition for what's going on by appealing to Euler integration
# the power series is nice because it *just works*, but the calculation often outpaces the understanding when you use it


class VecField(Scene):
    def construct(self):
        A = numpy.array([[0.0, -1.0], [1.0, 0.0]])
        Ax = lambda p: numpy.matmul(A, p[0: 2])
        vec_field = VectorField(Ax)

        self.play(FadeIn(vec_field))
        self.wait(2)