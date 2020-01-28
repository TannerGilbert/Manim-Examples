from manimlib.imports import *


class displayText(Scene):
    def construct(self):
        # Create TextMobjects
        first_line = TextMobject('Create cool animations')
        second_line = TextMobject('using Manim')
        third_line = TextMobject('Try it out yourself.', color=RED)

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.wait(2)