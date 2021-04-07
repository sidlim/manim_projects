from manim import *
import math, itertools, functools, random, numpy, logging

# Note to self: The only way to make this work is if you modularize it

# First thing to do: Write the animation for stepping a vector along a
# vector field by as much as needed (t, t/2, whatever)

# What that's going to look like:
# Vector field Ax, point x on the vector field
# draw Ax & then show rescale animation by t or t/2
# Show sum as a new point


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