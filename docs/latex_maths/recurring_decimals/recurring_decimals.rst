====================================================
Recurring Decimals
====================================================

| Recurring decimals ae limited here to denominators of 3, 6, 7, 9, 11. 
| This limits the number of possible recurring decimals to a total of 26.
| The worksheet can have up to 26 recurring decimal questions.

----

Sample recurring decimals worksheets
-------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      recdec_1_q
      ^^^
      :download:`pdf<worksheets/recdec_q.pdf>`
      :download:`tex<worksheets/recdec_q.tex>`

   .. grid-item-card::  

      recdec_1_ans
      ^^^
      :download:`pdf<worksheets/recdec_ans.pdf>`
      :download:`tex<worksheets/recdec_ans.tex>`

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  
      
      recdec_2_q
      ^^^
      :download:`pdf<worksheets/recdec_shuffled_q.pdf>`
      :download:`tex<worksheets/recdec_shuffled_q.tex>`

   .. grid-item-card::  
      
      recdec_2_ans
      ^^^
      :download:`pdf<worksheets/recdec_shuffled_ans.pdf>`
      :download:`tex<worksheets/recdec_shuffled_ans.tex>`


----

Latex templates
--------------------

| The LaTeX recurring decimals **question** template is below.
| :download:`recurring_decimals_worksheet_template.tex<makers/recurring_decimals_worksheet_template.tex>`

.. literalinclude:: makers/recurring_decimals_worksheet_template.tex
   :linenos:
   
| The LaTeX recurring decimals **answer** template is below.
| :download:`recurring_decimals_worksheet_ans_template.tex<makers/recurring_decimals_worksheet_ans_template.tex>`

.. literalinclude:: makers/recurring_decimals_worksheet_ans_template.tex
   :linenos:

| The diagram template is below.
| :download:`recurring_decimals_worksheet_diagram_template.tex<makers/recurring_decimals_worksheet_diagram_template.tex>`

.. literalinclude:: makers/recurring_decimals_worksheet_diagram_template.tex
   :linenos:

| The diagram answer template is below.
| :download:`recurring_decimals_worksheet_diagram_ans_template.tex<makers/recurring_decimals_worksheet_diagram_ans_template.tex>`

.. literalinclude:: makers/recurring_decimals_worksheet_diagram_ans_template.tex
   :linenos:

----

Decimals python
-------------------

| The python below requires the 4 .tex files listed above.

| The 2 custom python modules required are:
| :download:`recurring_decimals_functions.py<makers/recurring_decimals_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

.. literalinclude:: makers/recurring_decimals_functions.py
   :linenos:

| The Python to create worksheets of questions involving recurring decimals, is below.
| :download:`recurring_decimals_worksheet_maker.py<makers/recurring_decimals_worksheet_maker.py>`

.. literalinclude:: makers/recurring_decimals_worksheet_maker.py
   :linenos:
