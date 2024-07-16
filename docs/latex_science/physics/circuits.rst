====================================================
Circuit circuitikz
====================================================

| See https://www.youtube.com/watch?v=WRTELZP1l0Y
| See: https://www.youtube.com/watch?v=eX3RTV97iZo
| See: https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ%3A_A_Tutorial_for_Beginners_(Part_4)%E2%80%94Circuit_Diagrams_Using_Circuitikz
| See: https://mirror.cse.unsw.edu.au/pub/CTAN/graphics/pgf/contrib/circuitikz/doc/circuitikzmanual.pdf

----

Simple series circuit
-------------------------

| A simple circuit is shown below.

.. figure:: files/circuit.png
   :width: 300
   :alt: circuit.png
   :figclass: align-center


.. literalinclude:: files/circuit.tex
   :linenos:

----

Latex guide
---------------------

| The **circuitikz** package is used to create circuit diagrams in LaTeX.
| It provides a set of macros and commands to draw circuit elements such as batteries, resistors, and capacitors.
| The **\draw** command is used to draw the circuit elements.
| The **to** keyword is used to connect the elements.
| The options within square brackets specify the type of element and its properties.

| The **to** keyword is used four times to connect circuit elements.
| The first **to** connects the bottom of the battery to the top **(0,0) to[battery={$12V$}] (0,2)**.
| The second **to** connects the top of the battery to a point **(2,2)** using a short wire **to[short] (2,2)**.
| The third **to** connects this point to a bulb with a resistance of 3 Ohms **to[bulb, l=$3\Omega$] (2,0)**.
| The fourth **to** connects the bottom of the bulb back to the bottom of the battery using a short wire **to[short] (0,0)**.

----

Series circuit with Ammeter and Voltmeter
-----------------------------------------

| A simple circuit is shown below.

.. figure:: files/circuit_globe_AV.png
   :width: 400
   :alt: circuit_globe_AV.png
   :figclass: align-center


.. literalinclude:: files/circuit_globe_AV.tex
   :linenos:

----

Series circuit with 2 globes
-----------------------------------------

| A series circuit with 2 globes.

.. figure:: files/circuit_2globes_series.png
   :width: 300
   :alt: circuit_2globes_series.png
   :figclass: align-center


.. literalinclude:: files/circuit_2globes_series.tex
   :linenos:

----


Parallel circuit with 2 globes
-----------------------------------------

| A parallel circuit with 2 globes.

.. figure:: files/circuit_2globes_parallel.png
   :width: 300
   :alt: circuit_2globes_parallel.png
   :figclass: align-center


.. literalinclude:: files/circuit_2globes_parallel.tex
   :linenos:

   