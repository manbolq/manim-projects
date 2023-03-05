from manimlib import *
from manim import *
import numpy as np


class FormulaColor1(Scene):
    def construct(self):
        texto = Tex('$x$', '$+$', '$1$', '$=$', '${1$', '$\\over$', '$2}$')
        texto[0].set_color(GREEN)
        texto[1].set_color(RED)
        texto[2].set_color(YELLOW)
        texto[3].set_color(WHITE)
        texto[4].set_color(BLUE)
        texto[5].set_color(GREY)
        self.play(Write(texto))


class CambioTamanio(Scene):
    def construct(self):
        texto = Tex("\\sum_{i=0}^n i=\\dfrac{n(n+1)}{2}")
        self.play(FadeIn(texto))
        self.wait()
        texto.scale(2)
        self.wait(2)
        self.play(FadeOut(texto))


class ColoreadoTexto(Scene):
    def construct(self):
        texto = Text("Texto u objeto")
        self.add(texto)
        self.wait(0.5)
        for letra in texto:
            self.play(LaggedStart(
                ApplyMethod, letra,
                lambda m: (m.set_color, YELLOW),
                run_time=0.12
            ))
        self.wait(0.5)


class Cuadrado(Scene):
    def construct(self):
        box = Rectangle(stroke_color=GREEN, stroke_opacity=0.7, fill_color=RED, fill_opacity=0.5, height=1, width=1)
        self.add(box)
        self.play(box.animate.shift(RIGHT * 2), run_time=2)
        self.play(box.animate.shift(UP * 3), run_time=2)
        self.play(box.animate.shift(LEFT * 5 + DOWN * 5), run_time=5)
        self.play(box.animate.shift(UP * 1.5 + RIGHT * 1), run_time=2)


class FittinObjects(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=12)

        circle = Circle(stroke_width=6, stroke_color=YELLOW, fill_color=RED_C, fill_opacity=0.8)
        circle.set_width(2).to_edge(DR, buff=0)

        triangulo = Triangle(stroke_color=ORANGE, stroke_widht=10, fill_color=GREY).set_height(2)

        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle, triangulo), run_time=3)


class Updaters(Scene):
    def construct(self):
        rectangulo = RoundedRectangle(stroke_width=8, stroke_color=WHITE, fill_color=BLUE_B, fill_opacity=0.2,
                                      width=4.5, height=2)
        rectangulo.shift(LEFT * 4 + UP * 3)

        texto = Tex("\\dfrac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
        texto.move_to(rectangulo.get_center())
        texto.add_updater(lambda x: x.move_to(rectangulo.get_center()))

        self.play(FadeIn(rectangulo))
        self.play(Write(texto))
        self.play(rectangulo.animate.shift(RIGHT * 2 + DOWN * 4), run_time=6)
        self.wait()
        texto.clear_updaters()
        self.play(rectangulo.animate.shift(RIGHT * 2 + UP * 4), run_time=6)


class Circulo(Scene):
    def construct(self):
        r = ValueTracker(0.5)  # Valor del radio que va cambiando

        circle = always_redraw(lambda: Circle(radius=r.get_value(), stroke_width=5, stroke_color=YELLOW))
        line_radius = always_redraw(lambda: Line(start=circle.get_center(), end=circle.get_bottom(), stroke_color=PINK,
                                                 stroke_width=3))
        triangle = always_redraw(lambda: Polygon(circle.get_top(), circle.get_left(), circle.get_right(),
                                                 stroke_color=BLUE, stroke_width=3))
        line_circ = always_redraw(lambda: Line(stroke_color=YELLOW, stroke_width=5).set_length(2*PI*r.get_value()).next_to(circle, DOWN, buff=0.2))

        # self.play(Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle), run_time=5)
        self.play(DrawBorderThenFill(circle))
        self.play(DrawBorderThenFill(line_radius))
        self.play(DrawBorderThenFill(triangle))

        self.play(ReplacementTransform(circle.copy(), line_circ), run_time=2)
        self.wait(2)
        self.play(r.animate.set_value(2), run_time=4)


class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 3, 1], x_length=5, y_length=3,
                    axis_config={"include_tip":True, "numbers_to_exclude":[0]}).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")
        graph = axes.get_graph(lambda x : x**0.5, x_range=[0, 4], color=YELLOW)
        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time=3)


class Graphing(Scene):
    def construct(self):
        my_plane = NumberPlane(x_range=[-6, 6, 2], x_length=5, y_range=[-10, 10, 2], y_length=5)
        my_plane.add_coordinates()

        my_function = my_plane.get_graph(lambda x : 0.1*x*(x-5)*(x+5), x_range=[-6, 6], color=GREEN_B)
        area = my_plane.get_area(my_function, x_range=[-5, 5], color=[BLUE, YELLOW])
        label = MathTex("f(x) = 0.1x(x-5)(x+5)").next_to(my_plane, UP, buff=0.2)

        self.play(DrawBorderThenFill(my_plane))
        self.play(Create(my_function), Write(label))
        self.play(FadeIn(area))
        self.wait(3)


class CoordSystem(Scene):
    def construct(self):

        dif_x = ValueTracker(1)

        plane = NumberPlane(x_range=[-4, 4, 1], x_length=4, y_range=[0, 20, 5], y_length=4).add_coordinates()
        plane.shift(DOWN*1.5+LEFT*3)
        plane_labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        plane_graph = plane.plot(lambda x : x**2, x_range=[-4, 4], color=YELLOW)
        area = always_redraw(lambda : plane.get_riemann_rectangles(graph=plane_graph, x_range=[-2, 2], dx=dif_x.get_value()))

        axes = Axes(x_range=[-4, 4], x_length=4, y_range=[-20, 20, 5], y_length=4).add_coordinates()
        axes.shift(RIGHT*3+DOWN*1.5)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f'(x)")
        axes_graph = axes.plot(lambda x : 2*x, x_range=[-4, 4], color=YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(graph=axes_graph, x_range=[-3, 3], num_lines=12)
        self.play(DrawBorderThenFill(plane), DrawBorderThenFill(axes))
        self.play(FadeIn(plane_labels))
        self.play(ReplacementTransform(plane_labels.copy(), axes_labels))
        self.wait()
        self.play(DrawBorderThenFill(plane_graph), DrawBorderThenFill(axes_graph), run_time=2)
        self.play(FadeIn(area), FadeIn(v_lines), run_time=2)
        for i in range(4):
            self.play(dif_x.animate.set_value(dif_x.get_value() / 2))
        self.wait(3)


class GraphPolar(Scene):
    def construct(self):
        e = ValueTracker(0.01)

        polar_plane = PolarPlane(radius_max=3).add_coordinates()
        polar_plane.shift(LEFT*3)
        graph1 = always_redraw(lambda :
                               ParametricFunction(lambda t : polar_plane.polar_to_point(2*np.sin(3*t), t),
                                                  t_range=[0, e.get_value()], color=GREEN)
                               )
        dot1 = always_redraw(lambda : Dot(fill_color=GREEN, fill_opacity=0.8,).scale(0.5).move_to(graph1.get_end()))

        axes = Axes(x_range=[0, 4], x_length=4, y_range=[-1.5, 1.5], y_length=3).add_coordinates()
        axes.shift(RIGHT*5)
        graph2 = always_redraw(lambda : axes.plot(lambda x : 2*np.sin(3*x), x_range=[0, e.get_value()]))
        dot2 = always_redraw(lambda : Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end()))

        title = MathTex(r"f(", "\\theta", r")", r"=", r"2", "\\sin", r"(", r"3", "\\theta", r")")
        title[1].set_color(GREEN)
        title[8].set_color(GREEN)
        title.next_to(axes, UP, buff=0.7)
        self.play(LaggedStart(DrawBorderThenFill(polar_plane), DrawBorderThenFill(axes), Write(title), lag_ratio=0.5,
                              run_time=3))
        self.add(graph1, graph2)
        self.play(e.animate.set_value(PI), run_time=5, rate_func=linear)
        self.wait(3)

class Colorear(Scene):
    def construct(self):
        title = MathTex(r"f(", "\\theta", r")", r"=", r"2", "\\sin", r"(", r"3", "\\theta", r")")
        title[1].set_color(GREEN)
        title[6].set_color(GREEN)

        self.add(title)


class Vectores(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3, -2], color=YELLOW)
        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector=vector)
        vector2 = self.add_vector([2, 2])
        self.write_vector_coordinates(vector=vector2)
        self.wait(3)


class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )

    def construct(self):
        matrix = [[1, 2], [2, 1]]
        matrix_tex = MathTex("A = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}").to_edge(UL).add_background_rectangle()

        unit_square = self.get_unit_square()
        text = always_redraw(lambda : MathTex("\\det A").set(width=0.7).move_to(unit_square.get_center()))

        vect = self.get_vector([1, -2], color=PURPLE_B)

        rect1 = Rectangle(width=1, height=2, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6).shift(UP*2+DOWN*2)
        circ1 = Circle(radius=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6).shift(LEFT*2+DOWN)
