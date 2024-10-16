====================================================
Check solutions to equations: 1 step diagrams
====================================================

| The python file to make a check_solution 1-step diagram is below.
| :download:`check_solution_diagram_maker.py<makers/check_solution_diagram_maker.py>`

| The required LaTeX files are below.
| :download:`check_solution_diagram_template.tex<makers/check_solution_diagram_template.tex>`
| :download:`check_solution_template.tex<makers/check_solution_template.tex>`

| The 2 custom python modules required are:
| :download:`check_solution_functions.py<makers/check_solution_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **check_solution_diagram_maker.py**, when run, will ask for these inputs:
| Choose the arithmetic process:
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n"``
| Choose the file name base:
| ``""Enter the base filename to be added to the prefix check_solution1_: \n"``
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.

----

Example check solution 1-step diagrams
-----------------------------------------

.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/check_solution1_+_q.png>`
      :download:`pdf<diagrams/check_solution1_+_q.pdf>`
      :download:`tex<diagrams/check_solution1_+_q.tex>`

      .. figure:: diagrams/check_solution1_+_q.png
         :width: 300
         :alt: check_solution1_+_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/check_solution1_+_ans.png>`
      :download:`pdf<diagrams/check_solution1_+_ans.pdf>`
      :download:`tex<diagrams/check_solution1_+_ans.tex>`

      .. figure:: diagrams/check_solution1_+_ans.png
         :width: 300
         :alt: check_solution1_+_ans
         :figclass: align-center


.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/check_solution1_-_q.png>`
      :download:`pdf<diagrams/check_solution1_-_q.pdf>`
      :download:`tex<diagrams/check_solution1_-_q.tex>`


      .. figure:: diagrams/check_solution1_-_q.png
         :width: 300
         :alt: check_solution1_-_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/check_solution1_-_ans.png>`
      :download:`pdf<diagrams/check_solution1_-_ans.pdf>`
      :download:`tex<diagrams/check_solution1_-_ans.tex>`

      .. figure:: diagrams/check_solution1_-_ans.png
         :width: 300
         :alt: check_solution1_-_ans
         :figclass: align-center


.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/check_solution1_x_q.png>`
      :download:`pdf<diagrams/check_solution1_x_q.pdf>`
      :download:`tex<diagrams/check_solution1_x_q.tex>`


      .. figure:: diagrams/check_solution1_x_q.png
         :width: 300
         :alt: check_solution1_x_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/check_solution1_x_ans.png>`
      :download:`pdf<diagrams/check_solution1_x_ans.pdf>`
      :download:`tex<diagrams/check_solution1_x_ans.tex>`

      .. figure:: diagrams/check_solution1_x_ans.png
         :width: 300
         :alt: check_solution1_x_ans
         :figclass: align-center


.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/check_solution1_div_q.png>`
      :download:`pdf<diagrams/check_solution1_div_q.pdf>`
      :download:`tex<diagrams/check_solution1_div_q.tex>`


      .. figure:: diagrams/check_solution1_div_q.png
         :width: 300
         :alt: check_solution1_div_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/check_solution1_div_ans.png>`
      :download:`pdf<diagrams/check_solution1_div_ans.pdf>`
      :download:`tex<diagrams/check_solution1_div_ans.tex>`

      .. figure:: diagrams/check_solution1_div_ans.png
         :width: 300
         :alt: check_solution1_div_ans
         :figclass: align-center

----

Check solution diagram: python
----------------------------------------------------------------------------

.. literalinclude:: makers/check_solution_diagram_maker.py
   :linenos:


Check solution diagram: LaTeX
----------------------------------------------------------------------------

.. literalinclude:: makers/check_solution_template.tex
   :linenos:

.. literalinclude:: makers/check_solution_diagram_template.tex
   :linenos:

