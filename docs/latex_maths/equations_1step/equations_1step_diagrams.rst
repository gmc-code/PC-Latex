====================================================
Equations 1 step diagrams
====================================================

| The python file to make a 1-step invop diagram is below.
| :download:`invop_diagram_maker.py<makers/invop_diagram_maker.py>`

| The required LaTeX files are below.
| :download:`invop_template.tex<makers/invop_template.tex>`
| :download:`invop_diagram_template.tex<makers/invop_diagram_template.tex>`

| The 2 custom python modules required are:
| :download:`invop_functions.py<makers/invop_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **invop_diagram_maker.py**, when run, will ask for these inputs:
| Choose the arithmetic process:
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 1st process"``
| Choose the file name base:
| ``"Enter the base filename to be added to the prefix :"``
| The prefix will be "involp1" for standard operations.
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.

----

Example 1-step invop diagram
-------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/invop1_+_q.png>`
      :download:`pdf<diagrams/invop1_+_q.pdf>`
      :download:`tex<diagrams/invop1_+_q.tex>`

      .. figure:: diagrams/invop1_+_q.png
         :width: 300
         :alt: invop1_+_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/invop1_+_ans.png>`
      :download:`pdf<diagrams/invop1_+_ans.pdf>`
      :download:`tex<diagrams/invop1_+_ans.tex>`

      .. figure:: diagrams/invop1_+_ans.png
         :width: 300
         :alt: invop1_+_ans
         :figclass: align-center

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/invop1_-_q.png>`
      :download:`pdf<diagrams/invop1_-_q.pdf>`
      :download:`tex<diagrams/invop1_-_q.tex>`


      .. figure:: diagrams/invop1_-_q.png
         :width: 300
         :alt: invop1_-_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/invop1_-_ans.png>`
      :download:`pdf<diagrams/invop1_-_ans.pdf>`
      :download:`tex<diagrams/invop1_-_ans.tex>`

      .. figure:: diagrams/invop1_-_ans.png
         :width: 300
         :alt: invop1_-_ans
         :figclass: align-center

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/invop1_x_q.png>`
      :download:`pdf<diagrams/invop1_x_q.pdf>`
      :download:`tex<diagrams/invop1_x_q.tex>`


      .. figure:: diagrams/invop1_x_q.png
         :width: 300
         :alt: invop1_x_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/invop1_x_ans.png>`
      :download:`pdf<diagrams/invop1_x_ans.pdf>`
      :download:`tex<diagrams/invop1_x_ans.tex>`

      .. figure:: diagrams/invop1_x_ans.png
         :width: 300
         :alt: invop1_x_ans
         :figclass: align-center

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<diagrams/invop1_div_q.png>`
      :download:`pdf<diagrams/invop1_div_q.pdf>`
      :download:`tex<diagrams/invop1_div_q.tex>`


      .. figure:: diagrams/invop1_div_q.png
         :width: 300
         :alt: invop1_div_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<diagrams/invop1_div_ans.png>`
      :download:`pdf<diagrams/invop1_div_ans.pdf>`
      :download:`tex<diagrams/invop1_div_ans.tex>`

      .. figure:: diagrams/invop1_div_ans.png
         :width: 300
         :alt: invop1_div_ans
         :figclass: align-center

----

1-step invop diagram: python
----------------------------------------------------------------------------

.. literalinclude:: makers/invop_diagram_maker.py
   :linenos:

| The custom python module:

.. literalinclude:: makers/invop_functions.py
   :linenos:

----

1-step invop diagram: LaTeX
----------------------------------------------------------------------------

.. literalinclude:: makers/invop_template.tex
   :linenos:

.. literalinclude:: makers/invop_diagram_template.tex
   :linenos:
