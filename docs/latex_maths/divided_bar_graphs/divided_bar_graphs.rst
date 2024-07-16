====================================================
Divided Bar graphs
====================================================

| Divided bar graphs are a bar graph in sections, which often total to 100. (100%)

| The python file to make divided bar graphs is below.
| :download:`divided_bar_chart_maker.py<files/divided_bar_chart_maker.py>`

| The required LaTeX files are below.
| :download:`divided_bar_chart_template.tex<files/divided_bar_chart_template.tex>`

| The custom python modules required are:
| :download:`magick_pdf_to_png.py<files/magick_pdf_to_png.py>`

| A sample text file is below:
| :download:`dbc_zoo.txt<files/dbc_zoo.txt>`


patterns
~~~~~~~~~~~~~~

| For patterns instead of filled colours use:

| The python file to make divided bar graphs is below.
| :download:`divided_bar_chart_patterns_maker.py<files/divided_bar_chart_patterns_maker.py>`

| The required LaTeX files are below.
| :download:`divided_bar_chart_patterns_template.tex<files/divided_bar_chart_patterns_template.tex>`

----

Python tools
------------------------

| A small python script to generate percetages summing ot 100%:

| :download:`num_sum_to_100_generator.py<python_tools/num_sum_to_100_generator.py>`

----

Example divided bar graphs
-------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      zoo
      ^^^
      :download:`png<files/dbc_zoo.png>`
      :download:`pdf<files/dbc_zoo.pdf>`
      :download:`tex<files/dbc_zoo.tex>`
      :download:`txt<files/dbc_zoo.txt>`


      .. figure:: files/dbc_zoo.png
         :width: 600
         :alt: dbc_zoo
         :figclass: align-center

   .. grid-item-card::

      participants
      ^^^
      :download:`png<files/dbc_participants.png>`
      :download:`pdf<files/dbc_participants.pdf>`
      :download:`tex<files/dbc_participants.tex>`
      :download:`txt<files/dbc_participants.txt>`


      .. figure:: files/dbc_participants.png
         :width: 600
         :alt: dbc_participants
         :figclass: align-center


.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      crust_elements
      ^^^
      :download:`png<files/dbc_crust_elements.png>`
      :download:`pdf<files/dbc_crust_elements.pdf>`
      :download:`tex<files/dbc_crust_elements.tex>`
      :download:`txt<files/dbc_crust_elements.txt>`


      .. figure:: files/dbc_crust_elements.png
         :width: 600
         :alt: dbc_crust_elements
         :figclass: align-center

   .. grid-item-card::

      icecream
      ^^^
      :download:`png<files/dbc_icecream.png>`
      :download:`pdf<files/dbc_icecream.pdf>`
      :download:`tex<files/dbc_icecream.tex>`
      :download:`txt<files/dbc_icecream.txt>`


      .. figure:: files/dbc_icecream.png
         :width: 600
         :alt: dbc_icecream
         :figclass: align-center


.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      outdoors
      ^^^
      :download:`png<files/dbc_outdoors.png>`
      :download:`pdf<files/dbc_outdoors.pdf>`
      :download:`tex<files/dbc_outdoors.tex>`
      :download:`txt<files/dbc_outdoors.txt>`

      .. figure:: files/dbc_outdoors.png
         :width: 300
         :alt: dbc_outdoors
         :figclass: align-center

   .. grid-item-card::  
      
      travel
      ^^^
      :download:`png<files/dbc_travel.png>`
      :download:`pdf<files/dbc_travel.pdf>`
      :download:`tex<files/dbc_travel.tex>`
      :download:`txt<files/dbc_travel.txt>`

      .. figure:: files/dbc_travel.png
         :width: 300
         :alt: dbc_travel
         :figclass: align-center

----

LaTeX
-------------

| The .tex file template is shown below.

.. literalinclude:: files/divided_bar_chart_template.tex
   :language: LaTeX

| The .tex file patterns template is shown below.

.. literalinclude:: files/divided_bar_chart_patterns_template.tex
   :language: LaTeX

----

Txt file
------------

| The .txt file is shown below.
| 3 lines store data:
| line 1: the plot title
| line 2: a comma separated sequence of numeric values
| line 3: a comma separated sequence of labels for the values

| A maximum number of entries for line 2 and line 3 is 10.
| Some characters need to be escaped manually such as \& for & and \% for % if used in line 1 or 3.


.. literalinclude:: files/dbc_zoo.txt
   :language: text

----

Png file
------------

| The .png file is shown below.

.. image:: files/dbc_zoo.png
    :width: 600

----

Python code
------------

| The python code is shown below.

.. literalinclude:: files/divided_bar_chart_maker.py
   :language: python

| The python code for patterns is the same as above except for the template used within it.

.. literalinclude:: files/divided_bar_chart_patterns_maker.py
   :language: python
