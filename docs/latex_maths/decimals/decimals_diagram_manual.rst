====================================================
Decimals diagram - manual
====================================================

| The LaTeX in this section is for a diagram for addition or subtraction of decimals.
| The values in the diagram can be entered manually into the LaTeX code.
| The snippet below from the LaTeX file shows a block in the preamble of the .tex file where the values for the backtacking diagram can be manually edited.

| The values in the braces, {}, can be manually set with up to 2 digits before the decimal point and up to 3 after it.
| The processes, ``\addsub`` can be ``+`` or ``-``.

.. code-block:: LaTeX

   % modify values
   \def\addsub{-}
   \def\deca{70.256}
   \def\decb{16.362}
   \def\answer{53.894}

| The line ``\begin{tabular}{d{2.3}}`` sets the spacing for up to 2 digits before and 3 digits after the decimal point.
| If more digits are required then the ``2`` and the ``3`` can be changed to suit.
| It uses the macro: ``\newcolumntype{d}[1]{D{.}{.}{#1}}`` which sets the decimal alignment and spacing.
| The command ``\newcolumntype{d}[1]{cD{.}{.}{#1}}`` defines a new column type `d` that takes a single argument specifying the number of decimal places. The `D` column type is defined by the `dcolumn` package and is used to align numeric columns on a decimal point. The first two arguments of `D` specify the input and output decimal separators, respectively. In this case, both are set to `.`. The third argument specifies the number of decimal places.

----

A decimals diagram with answers
--------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      question
      ^^^
      :download:`png<manual/decimal_man_q.png>`
      :download:`pdf<manual/decimal_man_q.pdf>`
      :download:`tex<manual/decimal_man_q.tex>`


      .. figure:: manual/decimal_mq.png
         :width: 300
         :alt: decimal_man_q
         :figclass: align-center

   .. grid-item-card::

      answer
      ^^^
      :download:`png<manual/decimal_man_ans.png>`
      :download:`pdf<manual/decimal_man_ans.pdf>`
      :download:`tex<manual/decimal_man_ans.tex>`

      .. figure:: manual/decimal_mans.png
         :width: 300
         :alt: decimal_man_ans
         :figclass: align-center

----

A decimals diagram LaTeX
------------------------------

| The manual question:

.. literalinclude:: manual/decimal_mq.tex
   :linenos:

| The manual answer:

.. literalinclude:: manual/decimal_mans.tex
   :linenos:


