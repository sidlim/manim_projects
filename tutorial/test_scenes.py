from manim import *

class FirstScene(Scene):
    def construct(self):
        text = TexMobject("\\binom{n}{k}")
        self.play(Write(text), run_time = 4)
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

class DotScene(Scene):
    def construct(self):
        obj = Dot()
        obj.to_edge(DOWN, buff = 0.4)
        self.add(obj)

class ColoredText(Scene):
    def construct(self):
        text = TextMobject("R", "O", "Y", "G", "B", "I", "V")
        text[0].set_color(RED)
        text[1].set_color(ORANGE)
        text[2].set_color(YELLOW)
        text[3].set_color(GREEN)
        text[4].set_color(BLUE)
        text[5].set_color(PURPLE)
        text[6].set_color(PURPLE)
        
        self.play(Write(text))
        self.wait(3)
        self.play(ApplyMethod(text.set_color, WHITE), run_time=2)
        self.wait(3)

class ConfigExample(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": BLUE
        },
        "text1": "Text 1"
        }
    def construct(self):
        t1 = TextMobject(self.text1)
        self.play(Write(t1))
        self.wait(3)

class Plot2DQuadratic(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "axes_color" : BLUE, 
        "x_axis_label" : "$t$",
        "y_axis_label" : "$f(t)$"
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    )
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()
    
    def setup_axes(self):
        GraphScene.setup_axes(self)
        
        init_label_x = 2
        end_label_x = 7
        step_x = 1
        
        init_label_y = 20
        end_label_y = 50
        step_y = 5
        
        self.x_axis.label_direction = DOWN
        self.y_axis.label_direction = LEFT
        
        self.x_axis.add_numbers(*range(init_label_x, end_label_x + step_x, step_x))
        self.y_axis.add_numbers(*range(init_label_y, end_label_y + step_y, step_y))
        
        self.play(Write(self.x_axis), Write(self.y_axis))

class Plot2DSinCos(GraphScene):
    CONFIG = {
        "x_min": -3 * PI / 2,
        "x_max": 3 * PI / 2,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "y_tick_frequency": 0.5,
        "x_tick_frequency": PI/2,
        "x_axis_label": None,
        "y_axis_label": None,
    }
    def construct(self):
        self.setup_axes()
        
        plotSin = self.get_graph(np.sin, color = GREEN, x_min = -4, x_max = 4)
        plotCos = self.get_graph(np.cos, color = GRAY, x_min = -PI, x_max = 0)
        
        plotSin.set_stroke(width=3)
        plotCos.set_stroke(width=2)
        
        for plot in (plotSin, plotCos):
            self.play(ShowCreation(plot), run_time = 2)
            self.wait(1)
        self.wait(2)
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        
        func = TexMobject("\\sin(\\theta)")
        var = TexMobject("\\theta")
        
        func.set_color(BLUE)
        var.set_color(PURPLE)
        
        func.next_to(self.y_axis, UP)
        var.next_to(self.x_axis, RIGHT)
        
        self.y_axis.label_direction = LEFT * 1.5
        self.y_axis.add_numbers(*[-1, 1])
        
        init_val_x = -3 * PI / 2
        step_x = PI/2
        end_val_x = 3*PI/2
        
        values_decimal_x = np.arange(init_val_x, end_val_x + step_x, step_x)
        
        list_x = TexMobject("-\\frac{3\\pi}{2}",
                            "-\\pi",
                            "-\\frac{\\pi}{2}",
                            "0",
                            "\\frac{\\pi}{2}",
                            "\\pi",
                            "\\frac{3\\pi}{2}")
        values_x = [(i,j) for i,j in zip(values_decimal_x, list_x)]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI:
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN)
            elif x_val == 0:
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN + LEFT)
            else:
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)
        
        self.play(*[Write(obj) for obj in [self.y_axis, self.x_axis, self.x_axis_labels, func, var]],
        run_time = 2)

class Plot3DBasic(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi = 80 * DEGREES, theta = 45 * DEGREES, distance = 10)
        self.play(ShowCreation(circle), ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate = 0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi = 30 * DEGREES, theta = 0 * DEGREES, distance = 8, run_time = 3)
        self.wait(3)

class ParametricCurve1(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(lambda u : np.array([
                 np.cos(u), np.sin(u), u/2]), color = RED, t_min = -TAU, t_max = TAU)
        curve2 = ParametricFunction(lambda u : np.array([
                 np.cos(u), np.sin(u), u]), color = RED, t_min = -TAU, t_max = TAU)
        axes = ThreeDAxes()
        
        self.add(axes)
        self.set_camera_orientation(phi = 80 * DEGREES, theta = -60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(FadeIn(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func = there_and_back, run_time = 3)
        self.wait()

class LabelPosUpdater(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")
        text.add_updater((lambda x: x.next_to(dot, RIGHT)))
        self.add(dot, text)
        self.play(dot.shift, UP*2)
        self.wait()
        self.play(dot.shift, UP*-2)

class NumberValUpdater(Scene):
    def construct(self):
        number_line = NumberLine(x_min = -1, x_max = 1)
        triangle = RegularPolygon(3, start_angle = -PI/2).scale(0.2).next_to(number_line.get_left(), UP)
        decimal = DecimalNumber(0, num_decimal_places = 2, include_sign = True, unit = None)
        decimal.add_updater(lambda d: d.next_to(triangle, UP * 0.5))
        decimal.add_updater(lambda d: d.set_value(triangle.get_center()[0]))
        
        self.add(number_line, triangle, decimal)
        self.play(triangle.shift, RIGHT*2, rate_func = there_and_back, run_time = 5)

class UpdateValueTracker(Scene):
    def construct(self):
        theta = ValueTracker(PI/2)
        line_1 = Line(ORIGIN, RIGHT*3, color = RED)
        line_2 = Line(ORIGIN, RIGHT*3, color = GREEN)
        
        line_2.add_updater(lambda m: m.set_angle(theta.get_value()))
        
        self.add(line_1, line_2)
        self.play(theta.increment_value, PI/2)
        self.wait()

class CustomRateFn(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(lambda u : np.array([
                 np.cos(u), np.sin(u), u/2]), color = RED, t_min = -TAU, t_max = TAU)
        curve2 = ParametricFunction(lambda u : np.array([
                 np.cos(u), np.sin(u), u]), color = RED, t_min = -TAU, t_max = TAU)
        axes = ThreeDAxes()
        
        self.add(axes)
        self.set_camera_orientation(phi = 80 * DEGREES, theta = -60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(FadeIn(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func = (lambda t: linear(1-t**2)), run_time = 3)
        self.wait()

class VecField(Scene):
    def construct(self):
        func = lambda p: np.array([0.5 * p[0] - 0.5 * p[1], (p[1])/2.0 + p[0]/2.0])
        vector_field_norm = VectorField(func)
        vector_field_unnorm = VectorField(func, length_func = linear)
        self.play(*[GrowArrow(vec) for vec in vector_field_norm])
        self.wait(3)
        self.play(ReplacementTransform(vector_field_norm, vector_field_unnorm))
        self.wait(3)

class ToEdgeAnimation(Scene):
    def construct(self):
        mob = Circle()
        
        self.add(mob)
        self.play(mob.scale, 2.0, mob.to_edge, {"buff": 0})
        self.wait(3)

class ToEdgeAnimation2(Scene):
    def construct(self):
        mob = Circle()
        
        self.add(mob)
        self.play(mob.to_edge, {"buff": 0}, mob.scale, 2.0)
        self.wait(3)

class TimeStepSceneTemplate(Scene):
    def setup(self):
        path = Line(LEFT * 6, RIGHT * 6)
        meterstick = VGroup()
        num_intervals = 60
        for i in range(num_intervals + 1):
            proportion = 1 / num_intervals
            tick = Line(DOWN * 0.3, UP * 0.3, stroke_width = 2)
            tick.move_to(path.point_from_proportion(proportion * i))
            meterstick.add(tick)
            if i in [i * num_intervals / 6 for i in range(0, 7)]:
                tick.set_stroke(BLUE)
                text = Text(f"{i}", font = "Arial", stroke_width = 0)
                text.set_height(0.5)
                text.next_to(tick, UP)
                self.add(text)
        meterstick.add(path)
        self.measure = meterstick
        self.measure.start = path.point_from_proportion(0)
        self.dot_distance = path.point_from_proportion(1/num_intervals) - path.point_from_proportion(0)
        self.dot = Dot(self.measure.start, color = BLUE)
        self.add(self.measure)

class TimeStepExScene1(TimeStepSceneTemplate):
    def construct(self):
        velocity = 15
        dt_length = 1.0 / self.camera.frame_rate
        
        self.update_ctr = 0
    
        def update_dot(d, dt):
            d.shift(RIGHT * self.dot_distance * dt * velocity)
            self.update_ctr += 1
            print(self.update_ctr)
        
        dot = self.dot
        self.add(dot)
        self.wait()
        dot.add_updater(update_dot)
        self.wait()
        dot.clear_updaters()
        self.wait()

class TimeStepExScene2(TimeStepSceneTemplate):
    CONFIG = {"velocity_factor": 15}
    def construct(self):
        self.dt_calculate = 1.0 / self.camera.frame_rate
        
        def update_dot(mob,dt):
            if dt == 0 and mob.counter==0:
                rate = self.velocity_factor * self.dt_calculate
                mob.counter += 1
            else:
                rate = dt * self.velocity_factor
            if dt > 0:
                mob.counter=0
            print(f"n: {mob.counter} - dt : {dt}")
            mob.shift(RIGHT * rate * self.dot_distance)
            mob.counter += 1
        
        dot = self.dot
        dot.counter = 0
        self.add(dot)
        self.wait()
        dot.add_updater(update_dot)
        self.wait()
        dot.clear_updaters()
        self.wait()

