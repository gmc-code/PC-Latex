====================================================
Chemistry chemfig LaTeX
====================================================

See: https://www.overleaf.com/learn/latex/Chemistry_formulae
See: https://mirror.aarnet.edu.au/pub/CTAN/macros/generic/chemfig/chemfig-en.pdf

| BingAi can be used to quickly get structural diagrams of chemicals by inlcuding "chemfig latex" in the prompt.
| Output latex can be copied and pasted into overleaf so that a pdf can be produced.
| e.g. prompt: write latex with chemfig for 20 organic compounds

----

chemfig
---------------

| The chemfig package makes it easy to draw structural diagrams of chemicals.


.. figure:: files/methane.png
   :width: 150
   :alt: methane
   :figclass: align-center

   methane

.. literalinclude:: files/methane.tex
   :linenos:


.. figure:: files/ethanol.png
   :width: 150
   :alt: ethanol
   :figclass: align-center

   ethanol

.. literalinclude:: files/ethanol.tex
   :linenos:


.. figure:: files/acetaldehyde.png
   :width: 150
   :alt: acetaldehyde
   :figclass: align-center

   acetaldehyde

.. literalinclude:: files/acetaldehyde.tex
   :linenos:


.. figure:: files/ethyne.png
   :width: 150
   :alt: ethyne
   :figclass: align-center

   ethyne

.. literalinclude:: files/ethyne.tex
   :linenos:



.. figure:: files/benzene.png
   :width: 150
   :alt: benzene
   :figclass: align-center

   benzene

.. literalinclude:: files/benzene.tex
   :linenos:


----


.. figure:: files/alanine.png
   :width: 150
   :alt: alanine
   :figclass: align-center

   alanine

.. literalinclude:: files/alanine.tex
   :linenos:


----

Pentane latex explained
-------------------------

.. figure:: files/pentane.png
   :width: 200
   :alt: pentane
   :figclass: align-center

   pentane

.. literalinclude:: files/pentane.tex
   :linenos:

| Pentane LaTeX uses a submolecule macro.
| The full LaTeX explanation is:

- `\documentclass[border = 1mm]{standalone}`: This sets the document class to `standalone`, which means that the output will be a single image file with a border of 1mm. This is useful for creating diagrams or figures that can be inserted into other documents.
- `\usepackage{chemfig}`: This loads the `chemfig` package, which provides commands and tools for drawing chemical structures and reactions.
- `\renewcommand*\printatom[1]{\ensuremath{\mathsf{#1}}}`: This line changes the font of the atoms to sans serif
- `\begin{document}`: This marks the beginning of the document content.
- `\definesubmol{C}{-C(-[2]H)(-[6]H)}`: This defines a sub-molecule named `C`, which consists of a carbon atom with two hydrogen atoms attached at angles of 2 and 6 (relative to the horizontal axis). This sub-molecule can be reused later in the code to simplify the drawing of larger molecules.
- `\chemfig{H!C!C!C!C!C-H}`: This draws a chemical structure using the `chemfig` syntax. The `!` symbol indicates that a sub-molecule is inserted at that position. So this code draws a hexane molecule, which is composed of six carbon atoms (using the sub-molecule `C`) and two hydrogen atoms at the ends.
- `\end{document}`: This marks the end of the document content.

----

Chemfig syntax
----------------

| ``\chemfig{<atom>-[<angle>,<length>,<side>,<style>]<atom>}``

| The <atom> argument is the name of the atom to be drawn. It can be a single letter or a group of letters enclosed in braces. For example, H, C, O, N, {CH3}, {OH}, etc.
| The - symbol is used to draw a single bond between two atoms. It can be replaced by other symbols to draw different types of bonds. For example, = for a double bond, ~ for a triple bond, etc.
| The [<angle>,<length>,<side>,<style>] argument is optional and can be used to modify the appearance of the bond. It can have up to four parameters separated by commas:

  - The <angle> parameter is a number that specifies the angle of the bond relative to the horizontal axis. It can be a multiple of 45 degrees (such as 2, 4, 6, 8) or an exact angle in degrees (such as 30, 60, 90). It can also be preceded by a colon (:) to indicate an absolute angle or a double colon (::) to indicate a relative angle. Positive angles are masured clockwise; negative, anticlockwise.
  - The <length> parameter is a number that specifies the length of the bond as a factor of the default length. For example, 2 means twice as long as the default length, 0.5 means half as long as the default length, etc.
  - The <side> parameter is either 1 or -1 and specifies which side of the bond the next atom will be drawn. For example, 1 means above the bond and -1 means below the bond.
  - The <style> parameter is a TikZ code that specifies the style of the bond. For example, dashed, dotted, red, thick, etc.

----

Ethylene syntax explained
-------------------------------

.. figure:: files/ethene.png
   :width: 300
   :alt: ethene
   :figclass: align-center

   ethene

.. literalinclude:: files/ethene.tex
   :linenos:

| `\chemfig{C(-[:120]H)(-[:240]H)=C(-[:300]H)-[:60]H}` represents a molecule of **ethene**.
| The syntax of the expression is as follows:

  - The **\chemfig** command starts drawing a molecular structure.
  - The **C** symbols represent carbon atoms.
  - The **H** symbols represent hydrogen atoms.
  - The **(-[:120]H)** means that there is a single bond (-) between the carbon atom and the hydrogen atom at an angle of 120 degrees from the horizontal axis. The angle is measured counterclockwise in multiples of 45 degrees, so 120 degrees is equivalent to [2.67] in the optional argument of the bond¹.
  - Similarly, the **(-[:240]H)** means that there is a single bond (-) between the carbon atom and the hydrogen atom at an angle of 240 degrees from the horizontal axis, or [5.33] in the optional argument of the bond¹.
  - The **=** symbol represents a double bond between two carbon atoms.
  - The **(-[:300]H)** means that there is a single bond (-) between the carbon atom and the hydrogen atom at an angle of 300 degrees from the horizontal axis, or [6.67] in the optional argument of the bond¹.
  - The **-[:60]H** means that there is a single bond (-) between the carbon atom and the hydrogen atom at an angle of 60 degrees from the horizontal axis, or [1.33] in the optional argument of the bond¹.

----

Lewis dot diagram
--------------------

.. figure:: files/water_lewis.png
   :width: 300
   :alt: water_lewis
   :figclass: align-center

   water_lewis

.. literalinclude:: files/water_lewis.tex
   :linenos:


.. figure:: files/hydronium_lewis.png
   :width: 300
   :alt: hydronium_lewis
   :figclass: align-center

   hydronium_lewis

.. literalinclude:: files/hydronium_lewis.tex
   :linenos:



----

Lewis equation
--------------------

.. figure:: files/lewis_equation.png
   :width: 600
   :alt: lewis_equation
   :figclass: align-center

   lewis_equation

.. literalinclude:: files/lewis_equation.tex
   :linenos:

----

Molecular equation
--------------------

.. figure:: files/molecular_equation.png
   :width: 600
   :alt: molecular_equation
   :figclass: align-center

   molecular_equation

.. literalinclude:: files/molecular_equation.tex
   :linenos:

