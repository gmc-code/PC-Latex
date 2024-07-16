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
      :download:`pdf<booklets/asdBk_add1dp_ans.pdf>`
      :download:`tex<booklets/asdBk_add1dp_ans.tex>`

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


.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random 5dp q
      ^^^
      :download:`pdf<booklets/asdBk_addsub5dp_q.pdf>`
      :download:`tex<booklets/asdBk_addsub5dp_q.tex>`

   .. grid-item-card::  

      random 5dp ans
      ^^^
      :download:`pdf<booklets/asdBk_addsub5dp_ans.pdf>`
      :download:`tex<booklets/asdBk_addsub5dp_ans.tex>`


----

Latex  templates
~~~~~~~~~~~~~~~~~~~~

| The multi page LaTeX decimals **question** template is below.
| :download:`add_sub_decimals_booklet_template<makers/add_sub_decimals_booklet_template.tex>`

.. literalinclude:: makers/add_sub_decimals_booklet_template.tex
   :linenos:
   
| The multi page LaTeX decimals **answer** template is below.
| :download:`add_sub_decimals_booklet_ans_template<makers/add_sub_decimals_booklet_ans_template.tex>`

.. literalinclude:: makers/add_sub_decimals_booklet_ans_template.tex
   :linenos:

| The diagram template is below.
| :download:`add_sub_decimals_booklet_diagram_template<makers/add_sub_decimals_booklet_diagram_template.tex>`

.. literalinclude:: makers/add_sub_decimals_booklet_diagram_template.tex
   :linenos:


| Here's what some parts of the diagram LaTeX do:

1. `\begin{equation}`: starts an equation environment.
2. `\raisebox{-0.85cm}{`: raises the following content by -0.85cm to move up the tabular diagram relative to the equation number.
3. `\begin{tabular}{d{4.5}}`: starts a tabular environment with decimal points aligned with room for 4 digits in front of it and 5 after it.
4. `<<num1>> \\`: adds the content of `<<num1>>` to the first row of the table and ends the row.
5. `<<process>>\enspace<<num2>> \\`: adds the content of `<<process>>` and `<<num2>>` separated by an en space to the second row of the table and ends the row.
6. `\hline`: adds a horizontal line to the table.
7. `<<answer>> \\`: adds the content of `<<answer>>` to the third row of the table and ends the row.
8. `\hline\\`: adds another horizontal line to the table and ends the row.
9. `\end{tabular}}`: ends the tabular environment.
10. `\end{equation}`: ends the equation environment.
