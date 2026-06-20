---
tags:
alias:
creation-date: Friday 3rd February 2023
last-modified-date: Friday 3rd February 2023 10:12:42
---
This five-part series of articles uses a combination of video and textual descriptions to teach the basics of creating LaTeX graphics using TikZ. These tutorials were first published on the original ShareLateX blog site during August 2013; consequently, today's editor interface (Overleaf) has changed considerably due to the development of ShareLaTeX and the subsequent merger of ShareLaTeX and Overleaf. However, much of the content is still relevant and teaches you some basic LaTeX—skills and expertise that will apply across all platforms.

<iframe src="https://www.youtube.com/embed/pcIzeN46ETc" width="600" height="338" frameborder="0" allowfullscreen=""></iframe>

[TikZ](http://cremeronline.com/LaTeX/minimaltikz.pdf) is a [LaTeX package](https://ctan.org/pkg/pgf?lang=en) that allows you to create high quality diagrams—and often quite complex ones too. In this first post we'll start with the basics, showing how to draw simple shapes, with subsequent posts introducing some of the interesting things you can do using the `tikz` package.

To get started with TikZ we need to load up the `tikz` package:

Now whenever we want to create a TikZ diagram we need to use the `tikzpicture` environment.

```LaTeX
\begin{tikzpicture}
<code goes here>
\end{tikzpicture}

```

### Basic shapes

One of the simplest and most commonly used commands in TikZ is the `\draw` command. To draw a straight line we use this command, then we enter a starting co-ordinate, followed by two dashes before the ending co-ordinate. We then finish the statement by closing it with a semicolon.

![Tiksline.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/2/20/Tiksline.png)

We can then add more co-ordinates in like this to make it a square:

```
\draw (0,0) -- (4,0) -- (4,4) -- (0,4) -- (0,0);

```

![Tikssquare.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/6/6d/Tikssquare.png)

However this isn't particularly good style. As we are drawing a line that ends up in the same place we started, it is better to finish the statement with the keyword `cycle` rather than the last co-ordinate.

```
\draw (0,0) -- (4,0) -- (4,4) -- (0,4) -- cycle;

```

To simplify this code further we can use the `rectangle` keyword after the starting co-ordinate and then follow it with the co-ordinate of the corner diagonally opposite.

```
\draw (0,0) rectangle (4,4);

```

We can also add lines that aren't straight. For example, this is how we draw a parabola:

```
\draw (0,0) parabola (4,4);

```

![Tiksparabola.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/a/a2/Tiksparabola.png)

To add a curved line we use _control points_. We begin with our starting co-ordinate, then use two dots followed by the keyword `controls` and then the co-ordinates of our control points separated by an `and`. Then after two more dots we have the final point. These control points act like magnets attracting the line in their direction:

```
\draw (0,0) .. controls (0,4) and (4,0) .. (4,4);

```

![Tikscurve.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/d/d9/Tikscurve.png)

We can then add a circle like this. The first co-ordinate is the circle's centre and the length in brackets at the end is the circle's radius:

```
\draw (2,2) circle (3cm);

```

![Tiksnicecircle.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/9/9b/Tiksnicecircle.png)

This is how we draw an ellipse. This time the lengths in the brackets separated by an `and`, are the x-direction radius and the y-direction radius respectively:

```
\draw (2,2) ellipse (3cm and 1cm);

```

![Tiksellipse.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/0/0b/Tiksellipse.png)

This is how we draw an arc. In the final bracket we enter the starting angle, the ending angle and the radius. This time they are separated by colons:

```
\draw (3,0) arc (0:75:3cm);

```

![Tiksarcsegment.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/2/26/Tiksarcsegment.png)

To customise the way these lines are drawn we add extra arguments into the `\draw` command. For example, we can edit the circle we drew so that the line is red, thick and dashed:

```
\draw[red,thick,dashed] (2,2) circle (3cm);

```

![Tiksredthickdashed.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/c/c0/Tiksredthickdashed.png)

### Grids

Very often when drawing diagrams we will want to draw a grid. To do this we use the `\draw` command followed by by some additional arguments. For example, we specify the grid step size using `step=` and a length. We've also specified the colour `gray` and told it to make the lines `very thin`. After these arguments we enter the co-ordinates of the bottom-left corner, followed by the keyword `grid` and then the co-ordinates of the top right-corner:

```
\draw[step=1cm,gray,very thin] (-2,-2) grid (6,6);

```

![Tiksgrid1.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/6/69/Tiksgrid1.png)

If we want to remove the outer lines around this grid we can crop the size slightly like this:

```
\draw[step=1cm,gray,very thin] (-1.9,-1.9) grid (5.9,5.9);

```

![Tiksgrid2.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/7/73/Tiksgrid2.png)

### Colour filling

Now lets add a shape onto our grid and colour it in. To do this we use the `\fill` command instead of the `\draw` command. Then in square brackets we enter a colour. For example, this specifies a colour that is 40% blue mixed with 60% white. Then we just specify a closed shape as we would normally:

```
\fill[blue!40!white] (0,0) rectangle (4,4);

```

![Tiksfill.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/3/3d/Tiksfill.png)

If we wanted to add a border around this shape we could change it to the `\filldraw` command and then alter the arguments so that we have both a fill colour and a draw colour specified:

```
\filldraw[fill=blue!40!white, draw=black] (0,0) rectangle (4,4);

```

![Tiksfilldraw.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/f/fe/Tiksfilldraw.png)

If instead of one solid colour we want a colour gradient, we could change it to the `\shade` command. Then in the square brackets we specify a left colour and a right colour:

```
\shade[left color=blue,right color=red] (0,0) rectangle (4,4);

```

![Tiksshade1.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/5/5c/Tiksshade1.png)

Instead of doing it from left to right we could do it from top to bottom:

```
\shade[top color=blue,bottom color=red] (0,0) rectangle (4,4);

```

![Tiksshade2.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/2/2c/Tiksshade2.png)

Or we could even change it by specifying an inner and outer colour like this:

```
\shade[inner color=blue,outer color=red] (0,0) rectangle (4,4);

```

![Tiksshade3.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/c/c5/Tiksshade3.png)

Finally we could also add a border to this by using the `\shadedraw` command and adding a draw colour:

```
\shadedraw[inner color=blue,outer color=red, draw=black] (0,0) rectangle (4,4);

```

![Tiksshadedraw.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/5/5a/Tiksshadedraw.png)

### Axes

Let's finish this post by adding some labeled axes to our grid. To do this we draw two normal lines both from (0,0), but we'll make them thick and add arrowheads using a dash and a pointed bracket:

```
\draw[thick,->] (0,0) -- (4.5,0);
\draw[thick,->] (0,0) -- (0,4.5);

```

![Tiksplainarrows.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/8/85/Tiksplainarrows.png)

We can also label our axes using _nodes_. To do this we add the keyword `node` into both `\draw` statements next to the end co-ordinates, followed by an `anchor` specification in square brackets and the text in curly brackets. Every `node` we create in TikZ has a number of anchors. So when we specify the `north west` anchor for the x-axis node, we are telling TikZ to use the anchor in the top-left-hand corner to anchor the node to the co-ordinate:

```
\draw[thick,->] (0,0) -- (4.5,0) node[anchor=north west] {x axis};
\draw[thick,->] (0,0) -- (0,4.5) node[anchor=south east] {y axis};

```

![Tiksnodes.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/b/b4/Tiksnodes.png)

To finish our axes we can add in ticks and numbering like this:

```
\foreach \x in {0,1,2,3,4}
   \draw (\x cm,1pt) -- (\x cm,-1pt) node[anchor=north] {$\x$};
\foreach \y in {0,1,2,3,4}
    \draw (1pt,\y cm) -- (-1pt,\y cm) node[anchor=east] {$\y$};

```

![Tiksforeach.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/9/9d/Tiksforeach.png)

This clever piece of code uses two `for each` loops to systematically go along the axes adding the ticks and numbers. In each one, the variable x or y takes on all of the numbers in the curly brackets, each in turn and executes the `\draw` command.

This concludes our discussion on basic drawing in TikZ. If you want to play around with the document we created in this post you can access it [here](https://www.sharelatex.com/project/521b4a1206bf09190f129751). In the [next post](https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ%3A_A_Tutorial_for_Beginners_(Part_2)%E2%80%94Generating_TikZ_Code_from_GeoGebra "LaTeX Graphics using TikZ: A Tutorial for Beginners (Part 2)—Generating TikZ Code from GeoGebra") we'll look exporting TikZ code from [GeoGebra](https://www.geogebra.org/?lang=en-GB).






