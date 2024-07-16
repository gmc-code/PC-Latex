====================================================
Backtracking 1-step worksheet LaTeX
====================================================

Sample 1-step backtracking worksheets by process
-------------------------------------------------------

.. grid:: 4
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      addition_q
      ^^^
      :download:`png<worksheets/bt1WS_+_q.png>`
      :download:`pdf<worksheets/bt1WS_+_q.pdf>`
      :download:`tex<worksheets/bt1WS_+_q.tex>`


      .. figure:: worksheets/bt1WS_+_q.png
         :width: 300
         :alt: bt1WS_+_q
         :figclass: align-center

   .. grid-item-card::  
      
      addition_ans
      ^^^
      :download:`png<worksheets/bt1WS_+_ans.png>`
      :download:`pdf<worksheets/bt1WS_+_ans.pdf>`
      :download:`tex<worksheets/bt1WS_+_ans.tex>`

      .. figure:: worksheets/bt1WS_+_ans.png
         :width: 300
         :alt: bt1WS_+_ans
         :figclass: align-center

   .. grid-item-card::  

      subtraction_q
      ^^^
      :download:`png<worksheets/bt1WS_-_q.png>`
      :download:`pdf<worksheets/bt1WS_-_q.pdf>`
      :download:`tex<worksheets/bt1WS_-_q.tex>`


      .. figure:: worksheets/bt1WS_-_q.png
         :width: 300
         :alt: bt1WS_-_q
         :figclass: align-center

   .. grid-item-card::  
      
      subtraction_ans
      ^^^
      :download:`png<worksheets/bt1WS_-_ans.png>`
      :download:`pdf<worksheets/bt1WS_-_ans.pdf>`
      :download:`tex<worksheets/bt1WS_-_ans.tex>`

      .. figure:: worksheets/bt1WS_-_ans.png
         :width: 300
         :alt: bt1WS_-_ans
         :figclass: align-center

.. grid:: 4
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      multiplication_q
      ^^^
      :download:`png<worksheets/bt1WS_x_q.png>`
      :download:`pdf<worksheets/bt1WS_x_q.pdf>`
      :download:`tex<worksheets/bt1WS_x_q.tex>`


      .. figure:: worksheets/bt1WS_x_q.png
         :width: 300
         :alt: bt1WS_x_q
         :figclass: align-center

   .. grid-item-card::  
      
      multiplication_ans
      ^^^
      :download:`png<worksheets/bt1WS_x_ans.png>`
      :download:`pdf<worksheets/bt1WS_x_ans.pdf>`
      :download:`tex<worksheets/bt1WS_x_ans.tex>`

      .. figure:: worksheets/bt1WS_x_ans.png
         :width: 300
         :alt: bt1WS_x_ans
         :figclass: align-center

   .. grid-item-card::  

      division_q
      ^^^
      :download:`png<worksheets/bt1WS_div_q.png>`
      :download:`pdf<worksheets/bt1WS_div_q.pdf>`
      :download:`tex<worksheets/bt1WS_div_q.tex>`


      .. figure:: worksheets/bt1WS_div_q.png
         :width: 300
         :alt: bt1WS_div_q
         :figclass: align-center

   .. grid-item-card::  
      
      division_ans
      ^^^
      :download:`png<worksheets/bt1WS_div_ans.png>`
      :download:`pdf<worksheets/bt1WS_div_ans.pdf>`
      :download:`tex<worksheets/bt1WS_div_ans.tex>`

      .. figure:: worksheets/bt1WS_div_ans.png
         :width: 300
         :alt: bt1WS_div_ans
         :figclass: align-center


----

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random_q
      ^^^
      :download:`png<worksheets/bt1WS_ran_q.png>`
      :download:`pdf<worksheets/bt1WS_ran_q.pdf>`
      :download:`tex<worksheets/bt1WS_ran_q.tex>`


      .. figure:: worksheets/bt1WS_ran_q.png
         :width: 300
         :alt: bt1WS_ran_q
         :figclass: align-center

   .. grid-item-card::  
      
      random_ans
      ^^^
      :download:`png<worksheets/bt1WS_ran_ans.png>`
      :download:`pdf<worksheets/bt1WS_ran_ans.pdf>`
      :download:`tex<worksheets/bt1WS_ran_ans.tex>`

      .. figure:: worksheets/bt1WS_x_ans.png
         :width: 300
         :alt: bt1WS_x_ans
         :figclass: align-center


----

Splitting the LaTeX and modifying it to be built by python
----------------------------------------------------------------

| The LaTeX from a single 1-step equation is used as a starting point, split into 2 and modified.
| The Worksheet template contains the preamble and the scaffold for the document.
| The Diagram template contains the backtacking diagram LaTeX.

Worksheet template
~~~~~~~~~~~~~~~~~~~~

| The LaTeX 1-step worksheet template is below.
| :download:`worksheet_template.tex<makers/backtrack_1step_worksheet_template.tex>`

.. literalinclude:: makers/backtrack_1step_worksheet_template.tex
   :linenos:

| ``\documentclass[leqno, 12pt]{article}`` specifies that you are working with an article document. The ``leqno`` option is used to place equation numbers on the left side of the equations instead of the right side. The ``12pt`` option sets the font size to 12 points.

| ``\usepackage{multicol}`` is a LaTeX package that allows multi-column layouts in documents. It defines the ``multicols`` environment, which takes one argument that specifies the total number of columns, such as ``\begin{multicols}{2}``.

| The page heading is set by: 
`\def \HeadingQuestions {\section*{\Huge Name: \underline{\hspace{8cm}} \hfill Date: \underline{\hspace{3cm}}}
{1-step backtracking: Questions} \vspace{1pt}\hrule}`

| The macro ``\HeadingQuestions`` creates a section heading with the text "Name: " in very large bold text with an underline, followed by an umderlined space of 8cm, followed by the text "Date: " in bold text with an underlined space of 3cm, followed by a horizontal line.

| ``\def`` is a LaTeX command that defines a macro, which is a custom command that performs a specific set of actions.
| ``\HeadingQuestions`` is the name of the macro being defined with the ``\def`` command.
| The ``\section*`` command is used to create a section heading without a number, and the ``\Huge`` command is used to make the heading text very large.
| The ``\underline`` command is used to add a horizontal line under its text.
| The ``\hspace`` command is used to add space on both sides of the heading text.
| The ``\hrule`` command is used to create a horizontal line, which separates the heading from the remainder of the document.

| ``\vspace{-5mm}`` is a command that adds vertical space to the document. The `-5mm` argument specifies that the space should be negative 5 millimeters. This means that the following text will be moved up by 5 millimeters.

| ``\begin{multicols}{2}`` command creates 2 columns. 

| The ``\columnbreak`` command is used to force a column break at that point in the document. The command works by creating a vertical white space, which is big enough to move the text from the top of the current column to the top of the next column.

| ``<<col1>>`` is placeholder text for the text that python will use to add the LaTeX for the backtracking diagrams in column 1.
| ``<<col2>>`` is placeholder text for column 2.

----

Diagram template
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The LaTeX 1-step diagram template for each diagram is below.
| :download:`diagram_template.tex<makers/backtrack_1step_worksheet_diagram_template.tex>`

.. literalinclude:: makers/backtrack_1step_worksheet_diagram_template.tex
   :linenos:
   
Question numbering 
~~~~~~~~~~~~~~~~~~~~~~

| ``\begin{equation}`` and the end tag wrap around the tikzpicture so that a question number is added.
| ``\begin{tikzpicture}[baseline={([yshift=-1pt]current bounding box.north)}]`` moves the tikzpicture and question number so that the question number is moved to the top left (set to the left in the documentclass).
| The option `baseline=(current bounding box.north)` aligns the top of the bounding box of the TikZ picture with the baseline of the surrounding text. 
| ``[yshift=-1pt]`` can be modified to adjust their relative laignment at the top.

Placeholders to be replaced by python 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The line ``\node[backtrack] (boxB) [right=1cm of boxA] {$<<boxB>>$}`` has a placeholder `<<boxB>>` which is replaced by python.
| Other placeholders are tagged by `<<   >>`.
