====================================================
Check solutions to equations: 2 step diagrams
====================================================

| The python file to make a check_solution 2-step diagram is below.
| :download:`check_solution_2step_diagram_maker.py<makers/check_solution_2step_diagram_maker.py>`

| The required LaTeX files are below.
| :download:`check_solution_2step_diagram_template.tex<makers/check_solution_2step_diagram_template.tex>`
| :download:`check_solution_2step_template.tex<makers/check_solution_2step_template.tex>`

| The 2 custom python modules required are:
| :download:`check_solution_functions.py<makers/check_solution_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **check_solution_2step_diagram_maker.py**, when run, will ask for these inputs:
| Choose the arithmetic process for the 1st process:
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 1st process"``
| Choose the arithmetic process for the 2nd process:
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 2nd process"``
| Choose the file name base:
| ``"Enter the base filename to be added to the prefix check_solution2_:"``
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.

----

Example check solution 2-step diagrams
-----------------------------------------

.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/check_solution2_+x_q.png>`
      :download:`pdf<diagrams/check_solution2_+x_q.pdf>`
      :download:`tex<diagrams/check_solution2_+x_q.tex>`

      .. figure:: diagrams/check_solution2_+x_q.png
         :width: 600
         :alt: check_solution2_+x_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/check_solution2_+x_ans.png>`
      :download:`pdf<diagrams/check_solution2_+x_ans.pdf>`
      :download:`tex<diagrams/check_solution2_+x_ans.tex>`

      .. figure:: diagrams/check_solution2_+x_ans.png
         :width: 600
         :alt: check_solution2_+x_ans
         :figclass: align-center


.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/check_solution2_div-_q.png>`
      :download:`pdf<diagrams/check_solution2_div-_q.pdf>`
      :download:`tex<diagrams/check_solution2_div-_q.tex>`


      .. figure:: diagrams/check_solution2_div-_q.png
         :width: 600
         :alt: check_solution2_div-_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/check_solution2_div-_ans.png>`
      :download:`pdf<diagrams/check_solution2_div-_ans.pdf>`
      :download:`tex<diagrams/check_solution2_div-_ans.tex>`

      .. figure:: diagrams/check_solution2_div-_ans.png
         :width: 600
         :alt: check_solution2_div-_ans
         :figclass: align-center

----

 Check solution 2step diagram: python
----------------------------------------------------------------------------

.. literalinclude:: makers/check_solution_2step_diagram_maker.py
   :linenos:

| The custom python module:

.. literalinclude:: makers/check_solution_functions.py
   :linenos:

----

Check solution 2step diagram: LaTeX
----------------------------------------------------------------------------

.. literalinclude:: makers/check_solution_2step_template.tex
   :linenos:

.. literalinclude:: makers/check_solution_2step_diagram_template.tex
   :linenos:

