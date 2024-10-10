from manim import *
import numpy as np

class grafico(Scene):
    def construct (self):
        ejes = Axes(tips=False,x_range=[0,26,2],y_range=[0,16,2], axis_config={"include_numbers":True, "color":BLUE,})
        graph = ejes.plot(lambda x: 0.5*x, x_range=[0, 26], color=RED)
        
        self.play(Create(ejes),run_time = 1.5)
        self.wait(0.35)
        self.play(Create(graph))
        self.wait(0.4)

        rectangulos = VGroup()
        arealista2 = VGroup()
        texto = MathTex("y=","\dfrac{1}{2}{x}",color=RED).shift(RIGHT*0.2)
        texto.set_color_by_tex("y=", WHITE)
        texto.to_corner(UL, buff= 2)
        arealista = []
        
        self.play(Create(texto))
        for dx in np.arange(2,0.2,-0.24):
            rects = ejes.get_riemann_rectangles(graph=graph,x_range=(2,24),dx = dx)
            rectangulos.add(rects)
            n = int((24- 2) / dx)
            x_vals = np.arange(2, 24, dx)
            area = sum(0.5*x * dx for x in x_vals)
            arealetra = str(area)
            arealista.append(arealetra[0:6])
        for n in range(len(arealista)):
            textoarea = MathTex("Area="+arealista[n]).shift(UP*0.9)
            arealista2.add(textoarea)
        
        
        self.play(Create(rectangulos[0]),Create(arealista2[0]),run_time = 1.2)
        self.wait(0.8)
        
        for n in range(0,len(rectangulos)-1):
            self.play(Transform(rectangulos[n],rectangulos[n+1]),Transform(arealista2[n],arealista2[n+1]),run_time=1.22)
            self.remove(rectangulos[n],arealista2[n])
        
        
        rectsfinal = ejes.get_riemann_rectangles(graph=graph,x_range=(2,24),dx = 0.1, blend = True)
        valorfinal = MathTex("Area=143").shift(DOWN*1.76)
        
        
        self.play(Transform(rectangulos[len(rectangulos)-1],rectsfinal),Transform(arealista2[len(rectangulos)-1],valorfinal))
        self.wait(1.5)
        self.play(FadeOut(rectangulos[len(rectangulos)-1]),FadeOut(arealista2[len(rectangulos)-1]),FadeOut(ejes),run_time=1.5)