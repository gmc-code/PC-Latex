====================================================
Backtracking 1-step booklet python
====================================================

| The python below requires the following .tex files:
| :download:`backtrack_1step_booklet_template.tex<makers/backtrack_1step_booklet_template.tex>`
| :download:`backtrack_1step_booklet_ans_template.tex<makers/backtrack_1step_booklet_ans_template.tex>`
| :download:`backtrack_1step_booklet_diagram_template.tex<makers/backtrack_1step_booklet_diagram_template.tex>`

| The 2 custom python modules required are:
| :download:`backtracking_functions.py<makers/backtracking_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The Python to create a multi page booklet of 1-step backtracking booklets, with 10 backtracking diagrams per page, is below.
| :download:`backtracking_1step_booklet_maker.py<makers/backtracking_1step_booklet_maker.py>`

| The python file, **backtracking_1step_booklet_maker.py**, when run, will ask for these inputs:

- Choose the arithmetic process: ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random"``.
- Choose the number of questions form 1 to 100: ``"Enter the number of questions from 1 to 100"``
- Choose the file name base: ``"Enter the base filename to be added to the prefix bt1Bk_:"``. The filename will have "_q" added for the question booklet and "_ans" for the answer booklet.


| The Python to create a multi page booklet of 1-step backtracking booklets, with 10 backtracking diagrams per page, is below.

.. literalinclude:: makers/backtracking_1step_booklet_maker.py
   :linenos:

| The custom Python module that is required to work out the various texts for the diagrams, is below.

.. literalinclude:: makers/backtracking_functions.py
   :linenos:

