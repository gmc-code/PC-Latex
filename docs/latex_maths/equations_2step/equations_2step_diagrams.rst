====================================================
Equations 2 step diagrams
====================================================

| The python file to make a 2-step invop diagram is below.
| :download:`invop_2step_diagram_maker.py<makers/invop_2step_diagram_maker.py>`

| The required LaTeX files are below.
| :download:`invop_2step_template.tex<makers/invop_2step_template.tex>`
| :download:`invop_2step_diagram_template.tex<makers/invop_2step_diagram_template.tex>`

| The 2 custom python modules required are:
| :download:`invop_functions.py<makers/invop_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **invop_2step_diagram_maker.py**, when run, will ask for these inputs:
| Choose the arithmetic process:
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 1st process"``
| Choose the arithmetic process:
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 2nd process"``
| Choose the file name base:
| ``"Enter the base filename to be added to the prefix :"``
| The prefix will be "invop2" for standard operations.
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.

----

Example 2-step invop diagram
-------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/invop2_+x_q.png>`
      :download:`pdf<diagrams/invop2_+x_q.pdf>`
      :download:`tex<diagrams/invop2_+x_q.tex>`


      .. figure:: diagrams/invop2_+x_q.png
         :width: 300
         :alt: invop2_+x_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/invop2_+x_ans.png>`
      :download:`pdf<diagrams/invop2_+x_ans.pdf>`
      :download:`tex<diagrams/invop2_+x_ans.tex>`

      .. figure:: diagrams/invop2_+x_ans.png
         :width: 300
         :alt: invop2_+x_ans
         :figclass: align-center

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/invop2_div-_q.png>`
      :download:`pdf<diagrams/invop2_div-_q.pdf>`
      :download:`tex<diagrams/invop2_div-_q.tex>`


      .. figure:: diagrams/invop2_div-_q.png
         :width: 300
         :alt: invop2_div-_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/invop2_div-_ans.png>`
      :download:`pdf<diagrams/invop2_div-_ans.pdf>`
      :download:`tex<diagrams/invop2_div-_ans.tex>`

      .. figure:: diagrams/invop2_div-_ans.png
         :width: 300
         :alt: invop2_div-_ans
         :figclass: align-center


----

2-step invop diagram: python
----------------------------------------------------------------------------

.. literalinclude:: makers/invop_2step_diagram_maker.py
   :linenos:

| The custom python module:

.. literalinclude:: makers/invop_functions.py
   :linenos:

----

2-step invop diagram: LaTeX
----------------------------------------------------------------------------

.. literalinclude:: makers/invop_2step_template.tex
   :linenos:

.. literalinclude:: makers/invop_2step_diagram_template.tex
   :linenos:
