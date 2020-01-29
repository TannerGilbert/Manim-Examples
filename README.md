# Manim Examples

[![Manim create graph video](https://img.youtube.com/vi/I0MwXnKSIAM/maxresdefault.jpg)](https://youtu.be/I0MwXnKSIAM)

## Table of Contents

TODO

## Installation

To install Manim, execute the following commands:

```bash
git clone https://github.com/3b1b/manim.git
pip3 install manimlib
python3 -m pip install -r requirements.txt
```

If you want to use LaTeX to display math you'll also need some further packages installed:
* [cairo](https://www.cairographics.org/) 
* [ffmpeg](https://www.ffmpeg.org/)
* [sox](http://sox.sourceforge.net/)
* [latex](https://www.latex-project.org/)

### Linux Installation

On Linux you can install these requirements with the following commands:

```bash
sudo apt install ffmpeg sox
sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev
sudo apt install texlive-latex-base texlive-full texlive-fonts-extra
```

### Windows Installation

On Windows the installation is a little bit more involved.

1. [Install FFmpeg.](https://www.wikihow.com/Install-FFmpeg-on-Windows)
2. [Install Cairo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo). For most users, pycairo‑1.18.0‑cp37‑cp37m‑win32.whl will do fine.
3. Install a LaTeX distribution. [MiKTeX](https://miktex.org/download) is recommended.
4. [Install SoX](https://sourceforge.net/projects/sox/files/sox/).
5. Install the remaining Python packages. Make sure that pycairo==1.17.1 is changed to pycairo==1.80.0 in requirements.txt.

```bash
git clone https://github.com/3b1b/manim.git
cd manim
pip3 install -r requirements.txt
python3 manim.py example_scenes.py SquareToCircle -pl
```

## Running Manim projects

An easy way to test whether your installation is working is by running the following command:

```bash
python3 -m manim example_scenes.py SquareToCircle -pl
```

The -p flag in the command above stands for previewing. The -l flag is for faster rendering with lower quality.

## Live Streaming

You can also stream your animation by running manim with the --livestream option.

```bash
> python -m manim --livestream
Writing to media/videos/scene/scene/1080p30/LiveStreamTemp.mp4

Manim is now running in streaming mode. Stream animations by passing
them to manim.play(), e.g.
>>> c = Circle()
>>> manim.play(ShowCreation(c))

>>>
```

## Creating your first Scene

Now that you have installed everything correctly you're ready to write your first application. 

```python
from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()

        #Showing shapes
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

```bash
python3 -m manim square_to_circle.py SquareToCircle
```

[![Manim square to circle](https://img.youtube.com/vi/f6cvI-gxWP8/maxresdefault.jpg)](https://youtu.be/f6cvI-gxWP8)

Lets break this down step-by-step:
* The import statement on top imports everything needed to use Manim. 
* For running animations, you have to create a class that inherits from Manims Scene class.
* Inside the class you need to create the construct method. The construct method is essentially the main method for the class. In it you can write all the code for the animation.
* Inside the construct method I first created two MObjects (Manim Objects) – a circle and a square. Lastly I displayed the shapes using the play method.

We can also modify the appearance of the objects by adding a few lines of code:

```python
from manimlib.imports import *

class SquareToCircleWithModifications(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

[![Manim square to circle](https://img.youtube.com/vi/9R65QDHDGHU/maxresdefault.jpg)](https://youtu.be/9R65QDHDGHU)

## Displaying text

Displaying text is also pretty straight forward.

```python
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
```

In order to display text you need to create a TextMobject and pass it the text you want to write to the screen. After that you can display the text using the play method and some animation.

[![Manim display text](https://img.youtube.com/vi/J5-1t2ZxTrA/maxresdefault.jpg)](https://youtu.be/J5-1t2ZxTrA)

## Math equations

Math equations can be written in Manim using [LaTeX](https://www.latex-project.org/) – a typesetting system widely used in academia. On of LaTeX big advantages is that it allows you to create good looking math equation with an intuitive system.

I won't go over LaTeX in this article but if you are curious there are lots of great tutorials out there. 

Equations just like text can be created using TextMobjects. When making an equation you need to put a $ at the start and end of the text.

```python
text = TextMobject('some text')
equation = TextMobject('$some equation$')
```

You can add symbols like the summation or integral symbols with two backslashes.

```python
alpha = TextMobject('$\\alpha$')
```

Displaying some text and an equation could look like the following:

```python
from manimlib.imports import *


class displayEquations(Scene):
    def construct(self):
        # Create TextMobjects
        first_line = TextMobject('Manim also allows you')
        second_line = TextMobject('to show beautiful math equations')
        equation = TextMobject('$d\\left(p, q\\right)=d\\left(q, p\\right)=\\sqrt{(q_1-p_1)^2+(q_2-p_2)^2+...+(q_n-p_n)^2}=\\sqrt{\\sum_{i=1}^n\\left(q_i-p_i\\right)^2}$')
        
        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text and equation
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, equation), FadeOut(second_line))
        self.wait(3)
```

[![Manim display text](https://img.youtube.com/vi/E52oMYpL7A8/maxresdefault.jpg)](https://youtu.be/E52oMYpL7A8)

## Creating graphs

Manim also allows us to create and display graphs. For this you need to create a class that inherits from the GraphScene class. Furthermore, you need to specify a config dictionary that contains the most basic configuration of the graph.

The defaults look as follows:

```python
CONFIG = {
    "x_min": -1,
    "x_max": 10,
    "x_axis_width": 9,
    "x_tick_frequency": 1,
    "x_leftmost_tick": None,  # Change if different from x_min
    "x_labeled_nums": None,
    "x_axis_label": "$x$",
    "y_min": -1,
    "y_max": 10,
    "y_axis_height": 6,
    "y_tick_frequency": 1,
    "y_bottom_tick": None,  # Change if different from y_min
    "y_labeled_nums": None,
    "y_axis_label": "$y$",
    "axes_color": GREY,
    "graph_origin": 2.5 * DOWN + 4 * LEFT,
    "exclude_zero_label": True,
    "default_graph_colors": [BLUE, GREEN, YELLOW],
    "default_derivative_color": GREEN,
    "default_input_color": YELLOW,
    "default_riemann_start_color": BLUE,
    "default_riemann_end_color": GREEN,
    "area_opacity": 0.8,
    "num_rects": 50,
}
```

After specifying the config you can create a graph inside the construct method.

```python
from manimlib.imports import *


class CreateGraph(GraphScene):
    CONFIG = {
        'x_min': -3,
        'x_max': 3,
        'y_min': -5,
        'y_max': 5,
        'graph_origin': ORIGIN,
        'axes_color': BLUE
    }

    def construct(self):
        # Create Graph
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x**2, WHITE)
        graph_label = self.get_graph_label(graph, label='x^{2}')

        graph2 = self.get_graph(lambda x: x**3, WHITE)
        graph_label2 = self.get_graph_label(graph2, label='x^{3}')

        # Display graph
        self.play(ShowCreation(graph), Write(graph_label))
        self.wait(1)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(1)
```

[![Manim display text](https://img.youtube.com/vi/I0MwXnKSIAM/maxresdefault.jpg)](https://youtu.be/I0MwXnKSIAM)

As you can see to create a graph you need to create a method that returns a y value for every x value it gets. In the code above I used lambda functions to specify them but you can also use any other method. After you have created the method you need to pass it to self.get_graph, which creates a mobject out of the method.

Note that the method only specifies how the graph should look like and doesn't actually calculate any values yet. The amount of points, which are calculated are determined by the CONFIG dictionary specified above the construct method.

## Author
 **Gilbert Tanner**