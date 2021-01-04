from manim import *


class displayText(Scene):
    def construct(self):
        # Create Text objects
        first_line = Text('Create cool animations')
        second_line = Text('using Manim')
        third_line = Text('Try it out yourself.', color=RED)

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.wait(2)