====================================================
Graphs
====================================================

| Some simple graphs grids are below with some simple explanations of the code.

----


.. code-block:: LaTeX

    \documentclass[tikz, border = 3mm]{standalone}

    \begin{document}
    \begin{tikzpicture}

    % grid black help lines default colour is black!40
    \draw[help lines, step = 0.5cm] (-5, -5) grid (5, 5);

    % axis with end labels
    \draw[thick, <->] (0, -5.15) -- (0, 5.15) node[above] {$y$};
    \draw[thick, <->] (-5.15, 0) -- (5.15, 0) node[right] {$x$};

    \end{tikzpicture}
    \end{document}

Document
~~~~~~~~~~~~~~~~~~

| The command ``\documentclass[tikz, border = 3mm]{standalone}`` is used to create a standalone document that shrinks the page to just contains a single TikZ picture. 
| The tikz option tells LaTeX that we will be using TikZ to create the picture. 
| The border = 3mm option adds a 3mm border around the picture.

Help lines
~~~~~~~~~~~~~~~~~~

| The command ``\draw[help lines, step = 0.5cm] (-5, -5) grid (5, 5)`` is used to draw a grid of horizontal and vertical lines that are spaced 0.5cm apart. 
| The help lines option specifies that the lines should be thin and gray. 
| The ``step = 0.5cm`` option specifies the distance between the lines. 
| The coordinates ``(-5, -5)`` and ``(5, 5)`` specify the lower-left and upper-right corners of the grid.

Axes
~~~~~~~~~~~~~~~~~~

| The command ``\draw[thick, <->] (0, -5.15) -- (0, 5.15) node[above] {$y$}`` is used to draw a vertical line that extends from -5.1 to 5.1 on the y-axis. 
| The thick option specifies that the line should be drawn with a thick stroke. 
| The ``<->`` option specifies that arrowheads should be added to both ends of the line. 
| The ``(0, -5.15)`` and ``(0, 5.15)`` specify the starting and ending points of the line. 
| The ``node[above] {$y$}`` adds a label "y" above the line.


----

Setting font size for a node
--------------------------------

| The command ``\fontsize{7}{10}\selectfont`` sets the font size to 7pt and the baseline skip to 10pt. 
| The first argument specifies the font size and the second argument specifies the baseline skip. 
| The ``\selectfont`` command is used to activate the new font size.


