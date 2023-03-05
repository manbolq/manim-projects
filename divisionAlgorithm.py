from manimlib import *
from manim import *
import numpy as np


class IntegralDivision1(Scene):
    def construct(self):
        # formula = MathTex("\\int {f'(x) \\over f(x)} dx = \\ln |f(x)| + C")
        # titulo = Text("Una fórmula nos dice que").next_to(formula, UP, buff=1)
        # self.play(Write(titulo))
        # self.add(formula)
        # self.play(Write(MathTex("\\text{pero, ¿qué pasa si no se puede conseguir} ~ f'(x) ~ \\text{en el numerador?}").next_to(formula, DOWN, buff=1)))
        #
        # self.wait(3)
        # self.clear()
        # self.play(Write(Text("Cuando esto pase, vamos a distinguir dos casos: ").move_to(UP).set_width(10)))
        # self.play(Write(Tex('$\\bullet$ El grado del numerador es mayor (o igual) que el del denominador \\\\',
        #                         '$\\bullet$ El grado del numerador es menor que el del denominador \\\\').set_width(11)))
        # self.wait(4)
        # self.clear()
        #
        caso1 = Text("Primer caso").to_edge(UL).scale(0.6)
        self.add(caso1)

        texto_aux = Text("En este caso, tenemos que dividir los dos polinomios. Por ejemplo:").scale(0.5)
        texto_aux2 = Text("En este caso, tenemos que dividir los dos polinomios. Por ejemplo:").to_edge(UL).scale(0.3).shift(2*LEFT)
        self.play(Write(texto_aux))
        self.wait()
        self.play(ReplacementTransform(texto_aux, texto_aux2))
        polinomio1_texto = "x^4 + 3x^3 + 6x^2 -2x"
        polinomio2_texto = "x^2 - 4"
        polinomio1 = MathTex(polinomio1_texto)
        polinomio2 = MathTex(polinomio2_texto)
        texto_aux = MathTex("\\int {", polinomio1_texto, "\\over", polinomio2_texto, "} dx")
        texto_aux2 = MathTex("\\int {x^4 + 3x^3 + 6x^2 - 2x \\over x^2 -4} dx").scale(0.4).next_to(caso1, DOWN)
        self.play(Write(texto_aux))
        self.wait()
        self.play(ReplacementTransform(texto_aux, texto_aux2))

        linea_vert = Line(color=WHITE, stroke_width=4).set_length(0.8).rotate(PI/2).next_to(polinomio2, LEFT, buff=0.1)
        linea_hor = Line(color=WHITE, stroke_width=4).set_length(1.6).next_to(polinomio2, DOWN, buff=0.16)
        polinomio1.next_to(polinomio2, LEFT, buff=0.5)
        division = VGroup(polinomio1, polinomio2, linea_vert, linea_hor).shift(UP*1.5)
        self.add(division)
        self.wait()

        circulo1 = Circle(stroke_color=RED, stroke_width=2, radius=0.37).move_to(polinomio2.get_center()).shift(LEFT*0.45)
        circulo2 = Circle(stroke_color=RED, stroke_width=2, radius=0.37).move_to(polinomio1.get_center()).shift(LEFT*2)
        self.add(circulo1)
        self.add(circulo2)
        self.wait()

        multiplicacion = MathTex("x^2 \\cdot ? = x^4").next_to(division, RIGHT, buff=2)
        multiplicacion2 = MathTex("x^2 \\cdot x^2 = x^4").next_to(division, RIGHT, buff=2)
        self.play(ReplacementTransform(VGroup(circulo1.copy(), circulo2.copy()), multiplicacion), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(multiplicacion, multiplicacion2))
        self.play(FadeOut(circulo2, circulo1))
        primer_mon = MathTex("x^2").next_to(linea_hor, DOWN, buff=0.15).shift(LEFT*0.45)
        self.play(Write(primer_mon))
        self.wait()
        self.play(FadeOut(multiplicacion2))

        multiplicacion = MathTex("x^2 \cdot (x^2 -4) = ").next_to(division, RIGHT, buff=1)
        circulo2 = Circle(radius=0.37, stroke_color=RED, stroke_width=2).move_to(primer_mon.get_center())
        ovalo = Ellipse(width=1.7, height=1, stroke_color=RED, stroke_width=2).move_to(polinomio2.get_center())
        self.add(circulo2)
        self.add(ovalo)
        self.wait()
        self.play(ReplacementTransform(VGroup(circulo2, ovalo).copy(), multiplicacion))
        self.play(FadeOut(circulo2, ovalo))
        resultado = MathTex("x^4 - 4x^2").next_to(multiplicacion, RIGHT)
        self.wait(0.5)
        self.play(Write(resultado))
        resultado_restar = resultado.copy().next_to(polinomio1, DOWN).shift(LEFT*1.3)
        self.play(ReplacementTransform(resultado.copy(), resultado_restar))

        self.play(FadeOut(resultado, multiplicacion))
        linea_resta = Line(color=WHITE, stroke_width=4).set_length(4.7).move_to(resultado_restar.get_center()).shift(DOWN*0.5+RIGHT*1.3)
        self.play(Write(linea_resta))
        resultado_restar_signo = MathTex("-x^4 + 4x^2").next_to(polinomio1, DOWN).shift(LEFT*1.5)
        self.play(ReplacementTransform(resultado_restar, resultado_restar_signo))
        self.wait()

        resultado_resta = MathTex("3x^3 + 10x^2 - 2x").next_to(linea_resta, DOWN).shift(RIGHT*0.58)
        self.play(Write(resultado_resta))

        self.wait()

        circulo2 = Circle(stroke_color=RED, stroke_width=2, radius=0.45).move_to(resultado_resta.get_center()).shift(LEFT*1.35)
        self.add(circulo1)
        self.add(circulo2)
        self.wait()

        multiplicacion = MathTex("x^2 \\cdot ? = 3x^3").next_to(division, RIGHT, buff=2)
        multiplicacion2 = MathTex("x^2 \\cdot 3x = 3x^3").next_to(division, RIGHT, buff=2)
        self.play(ReplacementTransform(VGroup(circulo1.copy(), circulo2.copy()), multiplicacion), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(multiplicacion, multiplicacion2))
        self.play(FadeOut(circulo2, circulo1))
        segundo_mon = MathTex("x^2+3x").next_to(linea_hor, DOWN, buff=0.15).shift(RIGHT*0.11)
        self.play(ReplacementTransform(primer_mon, segundo_mon))
        self.play(FadeOut(multiplicacion2))

        circulo2 = Circle(radius=0.4, stroke_color=RED, stroke_width=2).move_to(segundo_mon.get_center()).shift(RIGHT*0.52)
        self.add(circulo2)
        self.add(ovalo)
        self.wait()

        multiplicacion = MathTex("3x \\cdot (x^2 -4) = ").scale(0.8).next_to(division, RIGHT, buff=1)

        self.play(ReplacementTransform(VGroup(circulo2, ovalo).copy(), multiplicacion))
        self.play(FadeOut(circulo2, ovalo))
        resultado = MathTex("3x^3 - 12x").scale(0.8).next_to(multiplicacion, RIGHT)
        self.wait(0.5)
        self.play(Write(resultado))

        resultado_resta2 = resultado.copy().scale(1.25).next_to(resultado_resta, DOWN).shift(LEFT*0.7)
        self.play(ReplacementTransform(resultado.copy(), resultado_resta2))

        linea_resta2 = Line(color=WHITE, stroke_width=4).set_length(3.7).move_to(resultado_resta2.get_center()).shift(DOWN*0.5+RIGHT*0.8)
        self.play(Write(linea_resta2))
        resultado_resta2_signo = MathTex("-3x^3 + 12x").move_to(resultado_resta2.get_center()).shift(LEFT*0.2)

        self.play(ReplacementTransform(resultado_resta2, resultado_resta2_signo))

        resultado_resta3 = MathTex("10x^2 + 10x").next_to(linea_resta2.get_center(), DOWN).shift(RIGHT*0.6)
        self.play(FadeOut(multiplicacion, resultado))
        self.play(Write(resultado_resta3))


        circulo2 = Circle(radius=0.53, stroke_color=RED, stroke_width=2).move_to(resultado_resta3.get_center()).shift(LEFT*0.73)
        self.add(circulo2)
        self.add(circulo1)
        self.wait()

        multiplicacion = MathTex("x^2 \\cdot ? = 10x^2").next_to(division, RIGHT, buff=2)
        multiplicacion2 = MathTex("x^2 \\cdot 10 = 10x^2").next_to(division, RIGHT, buff=2)
        self.play(ReplacementTransform(VGroup(circulo1.copy(), circulo2.copy()), multiplicacion), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(multiplicacion, multiplicacion2))
        self.play(FadeOut(circulo2, circulo1))

        tercer_mon = MathTex("x^2+3x+10").next_to(linea_hor, DOWN, buff=0.15).shift(RIGHT * 0.7)
        self.play(ReplacementTransform(segundo_mon, tercer_mon))
        self.play(FadeOut(multiplicacion2))

        circulo2 = Circle(radius=0.35, stroke_color=RED, stroke_width=2).move_to(tercer_mon.get_center()).shift(
            RIGHT*1.14)
        self.add(circulo2)
        self.add(ovalo)
        self.wait()

        multiplicacion = MathTex("10 \\cdot (x^2 -4) = ").scale(0.8).next_to(division, RIGHT, buff=1)

        self.play(ReplacementTransform(VGroup(circulo2, ovalo).copy(), multiplicacion))
        self.play(FadeOut(circulo2, ovalo))
        resultado = MathTex("10x^2 - 40").scale(0.8).next_to(multiplicacion, RIGHT)
        self.wait(0.5)
        self.play(Write(resultado))

        resultado_resta4 = resultado.copy().scale(1.25).next_to(resultado_resta3, DOWN).shift(LEFT*0.15)
        self.play(ReplacementTransform(resultado.copy(), resultado_resta4))
        self.play(FadeOut(multiplicacion, resultado))
        linea_resta3 = Line(color=WHITE, stroke_width=4).set_length(2.8).next_to(resultado_resta4, DOWN).shift(RIGHT*0.15)
        self.play(Write(linea_resta3))

        resultado_resta4_signo = MathTex("-10x^2 + 40").move_to(resultado_resta4.get_center()).shift(LEFT*0.2)
        self.play(ReplacementTransform(resultado_resta4, resultado_resta4_signo))

        resultado_resta5 = MathTex("10x + 40").next_to(linea_resta3, DOWN).shift(LEFT*0.25)
        self.play(Write(resultado_resta5))

        division_total = VGroup(division, resultado_restar_signo, linea_resta, tercer_mon, resultado_resta,
                                resultado_resta3, resultado_resta2_signo, linea_resta2, resultado_resta5, linea_resta3, resultado_resta4_signo)
        division_chica = division_total.scale(0.8).shift(UP*0.7+LEFT*1)
        # self.play(FadeTransform((division_total, division_chica)))
        self.play(ReplacementTransform(division_total, division_chica))

        dividendo = MathTex("x^4 + 3x^3 + 6x^2 - 2x = ").scale(0.8).next_to(linea_resta2, RIGHT, buff=1.1)
        # igual = Tex("=").next_to(dividendo, DOWN).scale(0.8).shift(LEFT*1.5)
        cociente = MathTex("= (x^2 + 3x + 10)").next_to(dividendo, RIGHT).scale(0.8)
        # por = Tex("\\cdot").next_to(cociente, RIGHT, buff=0.1).scale(0.8)
        divisor = MathTex("\\cdot (x^2 -4)").next_to(cociente, RIGHT).scale(0.8)
        # mas = Tex("+").next_to(divisor, RIGHT, buff=0.1).scale(0.8)
        resto = MathTex("+(10x+40)").next_to(divisor, RIGHT).scale(0.8)
        
        self.play(Write(dividendo))
        # self.play(Write(igual))
        self.play(Write(cociente))
        # self.play(Write(por))
        self.play(Write(divisor))
        # self.play(Write(mas))
        self.play(Write(resto))



        self.wait(3)