====================================================
Check solutions to equations: 1 step booklet python
====================================================

| The python file to make 1-step check solutions booklets is below.
| :download:`check_solution_booklet_maker.py<makers/check_solution_booklet_maker.py>`

| The required LaTeX files are below.
| :download:`check_solution_booklet_template.tex<makers/check_solution_booklet_template.tex>`
| :download:`check_solution_booklet_ans_template.tex<makers/check_solution_booklet_ans_template.tex>`
| :download:`check_solution_booklet_diagram_template.tex<makers/check_solution_booklet_diagram_template.tex>`
|

| The 2 custom python modules required are:
| :download:`check_solution_functions.py<makers/check_solution_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **check_solution_booklet_maker.py**, when run, will ask for these inputs:
| Choose the first arithmetic process: ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n"``
| Choose the number of questions from 1 to 100: ``"Enter the number of questions from 1 to 100; with 10 per page \n"``
| Choose the file name base: ``"Enter the base filename to be added to the prefix check_solution_Bk_: \n"``.
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.


    num1 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n")
----

Sample check solution booklet
-------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      addition_q
      ^^^
      :download:`pdf<booklets/check_solution_Bk_+_q.pdf>`
      :download:`tex<booklets/check_solution_Bk_+_q.tex>`

   .. grid-item-card::

      addition_ans
      ^^^
      :download:`pdf<booklets/check_solution_Bk_+_ans.pdf>`
      :download:`tex<booklets/check_solution_Bk_+_ans.tex>`

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      subtraction_q
      ^^^
      :download:`pdf<booklets/check_solution_Bk_-_q.pdf>`
      :download:`tex<booklets/check_solution_Bk_-_q.tex>`

   .. grid-item-card::

      subtraction_ans
      ^^^
      :download:`pdf<booklets/check_solution_Bk_-_ans.pdf>`
      :download:`tex<booklets/check_solution_Bk_-_ans.tex>`

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      multiplication_q
      ^^^
      :download:`pdf<booklets/check_solution_Bk_x_q.pdf>`
      :download:`tex<booklets/check_solution_Bk_x_q.tex>`

   .. grid-item-card::

      multiplication_ans
      ^^^
      :download:`pdf<booklets/check_solution_Bk_x_ans.pdf>`
      :download:`tex<booklets/check_solution_Bk_x_ans.tex>`

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      division_q
      ^^^
      :download:`pdf<booklets/check_solution_Bk_div_q.pdf>`
      :download:`tex<booklets/check_solution_Bk_div_q.tex>`

   .. grid-item-card::

      division_ans
      ^^^
      :download:`pdf<booklets/check_solution_Bk_div_ans.pdf>`
      :download:`tex<booklets/check_solution_Bk_div_ans.tex>`

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      random_q
      ^^^
      :download:`pdf<booklets/check_solution_Bk_ran_q.pdf>`
      :download:`tex<booklets/check_solution_Bk_ran_q.tex>`

   .. grid-item-card::

      random_ans
      ^^^
      :download:`pdf<booklets/check_solution_Bk_ran_ans.pdf>`
      :download:`tex<booklets/check_solution_Bk_ran_ans.tex>`

----

Check solution: python
----------------------------------------------------------------------------

.. literalinclude:: makers/check_solution_booklet_maker.py
   :linenos:


Check solution: LaTeX
----------------------------------------------------------------------------

.. literalinclude:: makers/check_solution_booklet_diagram_template.tex
   :linenos:

.. literalinclude:: makers/check_solution_booklet_template.tex
   :linenos:

.. literalinclude:: makers/check_solution_booklet_ans_template.tex
   :linenos:
