from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()

        #Showing shapes
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
