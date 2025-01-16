====================================================
Decimals booklet LaTeX
====================================================

Booklets
-------------------

Sample decimals booklets by process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::

        add 1dp q
        ^^^
        :download:`pdf<booklets/asdBk_add1dp_q.pdf>`
        :download:`tex<booklets/asdBk_add1dp_q.tex>`

    .. grid-item-card::

        add 1dp ans
        ^^^
        :download:`pdf<booklets/asdBK_add1dp_ans.pdf>`
        :download:`tex<booklets/asdBK_add1dp_ans.tex>`

.. grid:: 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::

        sub 2dp q
        ^^^
        :download:`pdf<booklets/asdBk_sub2dp_q.pdf>`
        :download:`tex<booklets/asdBk_sub2dp_q.tex>`

    .. grid-item-card::

        sub 2dp ans
        ^^^
        :download:`pdf<booklets/asdBk_sub2dp_ans.pdf>`
        :download:`tex<booklets/asdBk_sub2dp_ans.tex>`


----

Latex  templates
~~~~~~~~~~~~~~~~~~~~

| The multi page LaTeX decimals **question** template is below.
| :download:`decimals_booklet_template.tex<makers/decimals_booklet_template.tex>`

.. literalinclude:: makers/decimals_booklet_template.tex
   :linenos:

| The multi page LaTeX decimals **answer** template is below.
| :download:`decimals_booklet_ans_template.tex<makers/decimals_booklet_ans_template.tex>`

.. literalinclude:: makers/decimals_booklet_ans_template.tex
   :linenos:

| The diagram template is below.
| :download:`decimals_booklet_diagram_template.tex<makers/decimals_booklet_diagram_template.tex>`

.. literalinclude:: makers/decimals_booklet_diagram_template.tex
   :linenos:


| Here's what some parts of the diagram LaTeX do:


.. list-table:: Explanation of LaTeX code
   :widths: 50 50
   :header-rows: 1

   * - Line
     - Explanation
   * - ``\begin{equation}``
     - Begins the equation environment, which is used for displaying mathematical equations.
   * - ``\raisebox{-1.0cm}{``
     - Lowers the content inside the braces by 1.0 cm.
   * - ``\begin{tabular}{c d{<<numip>>.<<numdp>>}}``
     - Begins a tabular environment with two columns: the first column is centered (``c``), and the second column is aligned on the decimal point with specified integer and decimal places.
   * - ``&<<num1>> \tabularnewline``
     - Inserts the value of ``<<num1>>`` in the second column and moves to the next row.
   * - ``$<<process>>$&<<num2>> \tabularnewline``
     - Inserts the value of ``<<process>>`` in the first column (enclosed in math mode) and ``<<num2>>`` in the second column, then moves to the next row.
   * - ``\hline``
     - Adds a horizontal line across the table.
   * - ``&<<answer>> \tabularnewline``
     - Inserts the value of ``<<answer>>`` in the second column and moves to the next row.
   * - ``\hline``
     - Adds another horizontal line across the table.
   * - ``\end{tabular}}``
     - Ends the tabular environment and the ``\raisebox`` command.
   * - ``\end{equation}``
     - Ends the equation environment.

