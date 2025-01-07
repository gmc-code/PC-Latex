====================================================
Number Lines booklet LaTeX
====================================================

Multi page booklets
----------------------

| The Booklet code allows 8 diagrams per page, for up to 10 pages.

Examples: 2 pages of number lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      nlBk_plus_q
      ^^^
      :download:`pdf<booklets/nlBk_plus_q.pdf>`
      :download:`tex<booklets/nlBk_plus_q.tex>`

   .. grid-item-card::

      nlBk_plus_ans
      ^^^
      :download:`pdf<booklets/nlBk_plus_ans.pdf>`
      :download:`tex<booklets/nlBk_plus_ans.tex>`

   .. grid-item-card::

      nlBk_minus_neg_q
      ^^^
      :download:`pdf<booklets/nlBk_minus_neg_q.pdf>`
      :download:`tex<booklets/nlBk_minus_neg_q.tex>`

   .. grid-item-card::

      nlBk_minus_neg_ans
      ^^^
      :download:`pdf<booklets/nlBk_minus_neg_ans.pdf>`
      :download:`tex<booklets/nlBk_minus_neg_ans.tex>`

   .. grid-item-card::

      nlBk_minus_q
      ^^^
      :download:`pdf<booklets/nlBk_minus_q.pdf>`
      :download:`tex<booklets/nlBk_minus_q.tex>`

   .. grid-item-card::

      nlBk_minus_ans
      ^^^
      :download:`pdf<booklets/nlBk_minus_ans.pdf>`
      :download:`tex<booklets/nlBk_minus_ans.tex>`

   .. grid-item-card::

      nlBk_minus_pos_q
      ^^^
      :download:`pdf<booklets/nlBk_minus_pos_q.pdf>`
      :download:`tex<booklets/nlBk_minus_pos_q.tex>`

   .. grid-item-card::

      nlBk_minus_pos_ans
      ^^^
      :download:`pdf<booklets/nlBk_minus_pos_ans.pdf>`
      :download:`tex<booklets/nlBk_minus_pos_ans.tex>`

   .. grid-item-card::

      nlBk_plus_neg_q
      ^^^
      :download:`pdf<booklets/nlBk_plus_neg_q.pdf>`
      :download:`tex<booklets/nlBk_plus_neg_q.tex>`

   .. grid-item-card::

      nlBk_plus_neg_ans
      ^^^
      :download:`pdf<booklets/nlBk_plus_neg_ans.pdf>`
      :download:`tex<booklets/nlBk_plus_neg_ans.tex>`

   .. grid-item-card::

      nlBk_random_q
      ^^^
      :download:`pdf<booklets/nlBk_random_q.pdf>`
      :download:`tex<booklets/nlBk_random_q.tex>`

   .. grid-item-card::

      nlBk_random_ans
      ^^^
      :download:`pdf<booklets/nlBk_random_ans.pdf>`
      :download:`tex<booklets/nlBk_random_ans.tex>`


----

Splitting the LaTeX and modifying it to be built by python
----------------------------------------------------------------

| The LaTeX from a single number lines equation is used as a starting point, split into 2 and modified.
| The Booklet template contains the preamble and the scaffold for the document.
| The Diagram template contains the number line diagram LaTeX.

----

Booklet diagram template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The booklet diagram template is below.
| :download:`number_lines_booklet_diagram_template.tex<makers/number_lines_booklet_diagram_template.tex>`

.. literalinclude:: makers/number_lines_booklet_diagram_template.tex
   :linenos:

----

Booklet template
~~~~~~~~~~~~~~~~~~~~

| The multi page LaTeX number lines booklet template is below.
| :download:`number_lines_booklet_template.tex<makers/number_lines_booklet_template.tex>`

.. literalinclude:: makers/number_lines_booklet_template.tex
   :linenos:

| The multi page LaTeX number lines booklet answer template is below.
| :download:`number_lines_booklet_ans_template.tex<makers/number_lines_booklet_ans_template.tex>`

.. literalinclude:: makers/number_lines_booklet_ans_template.tex
   :linenos:

----

Footer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``\usepackage{fancyhdr}`` brings in the fancyhdr package  to control the position of the page number.
| The code below has been added to the preamble in LaTeX to move the page number up 6pt.

.. code-block:: LaTeX

   % raise footer with page number; no header
   \fancypagestyle{myfancypagestyle}{
      \fancyhf{}% clear all header and footer fields
      \renewcommand{\headrulewidth}{0pt} % no rule under header
      \fancyfoot[C] {\thepage} \setlength{\footskip}{14.5pt} % raise page number 6pt
   }
   \pagestyle{myfancypagestyle}


