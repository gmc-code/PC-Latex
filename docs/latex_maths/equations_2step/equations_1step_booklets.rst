====================================================
Equations 1-step booklet python
====================================================

| The python file to make 2-step backtracking booklets is below.
| :download:`backtracking_2step_booklet_maker.py<makers/backtracking_2step_booklet_maker.py>`

| The required LaTeX files are below.
| :download:`backtrack_2step_booklet_template.tex<makers/backtrack_2step_booklet_template.tex>`
| :download:`backtrack_2step_booklet_ans_template.tex<makers/backtrack_2step_booklet_ans_template.tex>`
| :download:`backtrack_2step_booklet_diagram_template.tex<makers/backtrack_2step_booklet_diagram_template.tex>`
| :download:`backtrack_2step_booklet_diagram_template_1buildexp.tex<makers/backtrack_2step_booklet_diagram_template_1buildexp.tex>`
| :download:`backtrack_2step_booklet_diagram_template_1invop.tex<makers/backtrack_2step_booklet_diagram_template_1invop.tex>`
| :download:`backtrack_2step_booklet_diagram_template_blank.tex<makers/backtrack_2step_booklet_diagram_template_blank.tex>`

| The 2 custom python modules required are:
| :download:`backtracking_functions.py<makers/backtracking_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **backtracking_2step_booklet_maker.py**, when run, will ask for these inputs:
| Choose the type of diagrams: 
| ``"Enter 1, 2, 3, 4, 5 or 6 for standard, 1 row build expression, 1 row inverse operations, 1 row from expression, solve from expression, blank "``
| Choose the first arithmetic process: ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 1st process"``.
| Choose the second arithmetic process: ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 2nd process"``
| Choose the number of questions from 1 to 100: ``"Enter the number of questions from 1 to 100"``
| Choose the file name base: ``"Enter the base filename to be added to the prefix bt2Bk_:"``. The filename will have "_q" added for the question booklet and "_ans" for the answer booklet.
| The prefix will be "bt2" for standard; "bt2_build" for 1 row build expression; or "bt2_invop" for 1 row inverse operations.
| The prefix will be "bt2_fromexp" for 1 row from expression; "bt2_solvefromexp" for solve from expression; or "bt2_blank" for blank.
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.

----

Sample 2-step backtracking booklet
-------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      multiplication_addition_q
      ^^^
      :download:`pdf<booklets/bt2Bk_X+_q.pdf>`
      :download:`tex<booklets/bt2Bk_X+_q.tex>`

   .. grid-item-card::  
      
      multiplication_addition_ans
      ^^^
      :download:`pdf<booklets/bt2Bk_X+_ans.pdf>`
      :download:`tex<booklets/bt2Bk_X+_ans.tex>`

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random_q
      ^^^
      :download:`pdf<booklets/bt2Bk_ran_q.pdf>`
      :download:`tex<booklets/bt2Bk_ran_q.tex>`

   .. grid-item-card::  
      
      random_ans
      ^^^
      :download:`pdf<booklets/bt2Bk_ran_ans.pdf>`
      :download:`tex<booklets/bt2Bk_ran_ans.tex>`

----

2-step backtracking: 1 row; building the expression
-------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random_q
      ^^^
      :download:`pdf<booklets/bt2Bk_build_ran_q.pdf>`
      :download:`tex<booklets/bt2Bk_build_ran_q.tex>`

   .. grid-item-card::  
      
      random_ans
      ^^^
      :download:`pdf<booklets/bt2Bk_build_ran_ans.pdf>`
      :download:`tex<booklets/bt2Bk_build_ran_ans.tex>`

----

2-step backtracking: 1 row; inverse operations
-------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random_q
      ^^^
      :download:`pdf<booklets/bt2Bk_invop_ran_q.pdf>`
      :download:`tex<booklets/bt2Bk_invop_ran_q.tex>`

   .. grid-item-card::  
      
      random_ans
      ^^^
      :download:`pdf<booklets/bt2Bk_invop_ran_ans.pdf>`
      :download:`tex<booklets/bt2Bk_invop_ran_ans.tex>`

----


2-step backtracking: 1 row; from the expression
-------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random_q
      ^^^
      :download:`pdf<booklets/bt2Bk_fromexp_ran_q.pdf>`
      :download:`tex<booklets/bt2Bk_fromexp_ran_q.tex>`

   .. grid-item-card::  
      
      random_ans
      ^^^
      :download:`pdf<booklets/bt2Bk_fromexp_ran_ans.pdf>`
      :download:`tex<booklets/bt2Bk_fromexp_ran_ans.tex>`

----


2-step backtracking: solve from the expression
-------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      random_q
      ^^^
      :download:`pdf<booklets/bt2Bk_solvefromexp_ran_q.pdf>`
      :download:`tex<booklets/bt2Bk_solvefromexp_ran_q.tex>`

   .. grid-item-card::  
      
      random_ans
      ^^^
      :download:`pdf<booklets/bt2Bk_solvefromexp_ran_ans.pdf>`
      :download:`tex<booklets/bt2Bk_solvefromexp_ran_ans.tex>`

----

2-step backtracking: python
----------------------------------------------------------------------------

.. literalinclude:: makers/backtracking_2step_booklet_maker.py
   :linenos:
