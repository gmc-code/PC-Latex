====================================================
Number Lines booklet LaTeX
====================================================

2 page booklets
-------------------

| The worksheet code can be modified to produce multipage booklets.
| The same diagram template can be used, without further modification.

2 page number lines examples
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

Worksheet template
~~~~~~~~~~~~~~~~~~~~

| The multi page LaTeX number lines worksheet template is below.
| :download:`worksheet_template.tex<makers/number_lines_worksheet_template.tex>`

.. literalinclude:: makers/number_lines_worksheet_template.tex
   :linenos:

| The multi page LaTeX number lines worksheet answer template is below.
| :download:`worksheet_template.tex<makers/number_lines_worksheet_ans_template.tex>`

.. literalinclude:: makers/number_lines_worksheet_ans_template.tex
   :linenos:

Modifications
~~~~~~~~~~~~~~~~

| ``\usepackage{fancyhdr}`` brings in the fancyhdr package  to control the position of the page number.
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
| The diagrams will still flow with 5 to a column since there is only just  room for 5, not 6.

.. code-block:: LaTeX

   \begin{multicols}{2}
      <<cols>>
   \end{multicols}

