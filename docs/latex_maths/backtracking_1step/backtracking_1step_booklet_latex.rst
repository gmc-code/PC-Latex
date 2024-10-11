====================================================
Backtracking 1-step booklet LaTeX
====================================================

2 page booklets
-------------------

| The worksheet code can be modified to produce multipage booklets.
| The same diagram template can be used, without further modification.

Sample 1-step backtracking booklets by process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 4
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      addition_q
      ^^^
      :download:`pdf<booklets/bt1Bk_+_q.pdf>`
      :download:`tex<booklets/bt1Bk_+_q.tex>`


   .. grid-item-card::

      addition_ans
      ^^^
      :download:`pdf<booklets/bt1Bk_+_ans.pdf>`
      :download:`tex<booklets/bt1Bk_+_ans.tex>`


   .. grid-item-card::

      subtraction_q
      ^^^
      :download:`pdf<booklets/bt1Bk_-_q.pdf>`
      :download:`tex<booklets/bt1Bk_-_q.tex>`


   .. grid-item-card::

      subtraction_ans
      ^^^
      :download:`pdf<booklets/bt1Bk_-_ans.pdf>`
      :download:`tex<booklets/bt1Bk_-_ans.tex>`


.. grid:: 4
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      multiplication_q
      ^^^
      :download:`pdf<booklets/bt1Bk_x_q.pdf>`
      :download:`tex<booklets/bt1Bk_x_q.tex>`


   .. grid-item-card::

      multiplication_ans
      ^^^
      :download:`pdf<booklets/bt1Bk_x_ans.pdf>`
      :download:`tex<booklets/bt1Bk_x_ans.tex>`


   .. grid-item-card::

      division_q
      ^^^
      :download:`pdf<booklets/bt1Bk_div_q.pdf>`
      :download:`tex<booklets/bt1Bk_div_q.tex>`


   .. grid-item-card::

      division_ans
      ^^^
      :download:`pdf<booklets/bt1Bk_div_ans.pdf>`
      :download:`tex<booklets/bt1Bk_div_ans.tex>`


.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      random_q
      ^^^
      :download:`pdf<booklets/bt1Bk_ran_q.pdf>`
      :download:`tex<booklets/bt1Bk_ran_q.tex>`


   .. grid-item-card::

      random_ans
      ^^^
      :download:`pdf<booklets/bt1Bk_ran_ans.pdf>`
      :download:`tex<booklets/bt1Bk_ran_ans.tex>`


----

Worksheet template
~~~~~~~~~~~~~~~~~~~~

| The multi page LaTeX 1-step worksheet **question** template is below.
| :download:`worksheet_question_template.tex<makers/backtrack_1step_booklet_template.tex>`

.. literalinclude:: makers/backtrack_1step_booklet_template.tex
   :linenos:

| The multi page LaTeX 1-step worksheet **answer** template is below.
| :download:`worksheet_answer_template.tex<makers/backtrack_1step_worksheet_ans_template.tex>`

.. literalinclude:: makers/backtrack_1step_worksheet_ans_template.tex
   :linenos:

Modifications
~~~~~~~~~~~~~~~~

| ``\usepackage{fancyhdr}`` brings in the fancyhdr package to control the position of the page number.
| The code below has been added to the preamble in LaTeX to move the page number up 6pt.

.. code-block:: LaTeX

   % raise footer with page number; no header
   \fancypagestyle{myfancypagestyle}{
      \fancyhf{}% clear all header and footer fields
      \renewcommand{\headrulewidth}{0pt} % no rule under header
      \fancyfoot[C] {\thepage} \setlength{\footskip}{6pt} % raise page number 6pt
   }
   \pagestyle{myfancypagestyle}

| The diagram placeholder has been simplified from two to just one.
| The diagrams will still flow with 5 to a column since there is only just room for 5, not 6.

.. code-block:: LaTeX

   \begin{multicols}{2}
      <<cols>>
   \end{multicols}

