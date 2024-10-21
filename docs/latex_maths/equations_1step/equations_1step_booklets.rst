====================================================
Equations 1-step booklet python
====================================================

| The python file to make 1-step invop booklets is below.
| :download:`invop_booklet_maker.py<makers/invop_booklet_maker.py>`

| The required LaTeX files are below.
| :download:`invop_booklet_template.tex<makers/invop_booklet_template.tex>`
| :download:`invop_booklet_ans_template.tex<makers/invop_booklet_ans_template.tex>`
| :download:`invop_booklet_diagram_template.tex<makers/invop_booklet_diagram_template.tex>`


| The 2 custom python modules required are:
| :download:`invop_functions.py<makers/invop_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **invop_booklet_maker.py**, when run, will ask for these inputs:
| Choose the first arithmetic process: ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random``.
| Choose the number of questions from 1 to 96: ``"Enter the number of questions from 1 to 96"``
| Choose the file name base: ``"Enter the base filename to be added to the prefix invop_Bk_:"``. The filename will have "_q" added for the question booklet and "_ans" for the answer booklet.

----

Sample 1-step invop booklet
-------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      random_q
      ^^^
      :download:`pdf<booklets/invop_Bk_ran96_q.pdf>`
      :download:`tex<booklets/invop_Bk_ran96_q.tex>`

   .. grid-item-card::

      random_ans
      ^^^
      :download:`pdf<booklets/invop_Bk_ran96_ans.pdf>`
      :download:`tex<booklets/invop_Bk_ran96_ans.tex>`

----

1-step invop: python
----------------------------------------------------------------------------

.. literalinclude:: makers/invop_booklet_maker.py
   :linenos:

| The custom python module:

.. literalinclude:: makers/invop_functions.py
   :linenos:

----

1-step invop: LaTeX
----------------------------------------------------------------------------

.. literalinclude:: makers/invop_booklet_diagram_template.tex
   :linenos:

.. literalinclude:: makers/invop_booklet_template.tex
   :linenos:

.. literalinclude:: makers/invop_booklet_ans_template.tex
   :linenos:
