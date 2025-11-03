====================================================
Producing images
====================================================

| There are multiple ways to produce high quality images from pdfs generated from LaTeX.
| The methods below are focussed on pdf to png conversion.
| The last method is the most efficient.

#. manual saving using Adobe Acrobat Pro.
#. in python via the subprocess module, or from the command line, both using ImageMagick.
#. in python, via the wand module, which requires ImageMagick installation.
#. in VSCode when building the pdf, via LaTeX Workshop extension, via a custom tool, a custom recipe calls a python script that uses ImageMagick.

.. admonition:: Tip

   The use of opacity in LaTeX is not handled well in the conversion of a pdf to png by the automated processes below, and so should be avoided.



----

Adobe Acrobat Pro
-------------------

| All pdfs produced as output from .tex files can be opened in Adobe Acrobat Pro.
| From within Adobe Acrobat Pro, use either File: Save As or File Export.
| Choose png as the file extension and click settings in the save dialog to choose 600 dpi for high quality results when the png is resized in Word.

----

ImageMagick
-----------------------

| Image Magick can be used to convert pdfs to jpgs or pngs from the **command line** or from **within python via the subprocess module**.
| For download see: https://imagemagick.org/script/download.php#windows
| For docs see: https://imagemagick.org/script/magick.php

| Download and install Image Magick.
| It's likely folder path is: ``C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/``
| Add the folder path to the Windows PATH Environment Variable.
| See how to add PATH variables:
| https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/

----

wand module
-----------------------

| The python module, wand, can be used to convert pdfs to jpgs or pngs from within python.
| Wand requires that ImageMagick is installed.
| See: https://pypi.org/project/Wand/
| See: https://docs.wand-py.org/en/0.6.13/wand/image.html#wand.image.Image

----

Sample python to convert a pdf to a png
--------------------------------------------

| An example of code to ``convert a pdf to a png`` is below.
| The full path of a pdf file needs to be pasted into the code.
| The full path to a pdf file can be obtained by right clicking on a file in the VSCode file explorer or by using the `Copy path` command in the ribbon in windows File Explorer.
| The choice of using magick or wand can be made using commenting and uncommenting in the python file.
| ``convert a pdf to a png.py`` uses two custom modules that have been designed to use similar syntax.
| The python files need to be in the same folder.

Downloads
~~~~~~~~~~~~

| To convert one pdf :download:`convert_pdf_to_png.py <../pdf_to_png_modules/convert_pdf_to_png.py>`.
| To convert a folder of pdfs :download:`folder_pdf_to_png.py <../pdf_to_png_modules/folder_pdf_to_png.py>`.
|
| Magick module file :download:`magick_pdf_to_png.py module <../pdf_to_png_modules/magick_pdf_to_png.py>`.
| Wand module file :download:`wand_pdf_to_png.py module <../pdf_to_png_modules/wand_pdf_to_png.py>`.

Python code
~~~~~~~~~~~~~~~~~~

| The folder_pdf_to_png.py file is shown below.

.. literalinclude:: ../pdf_to_png_modules/folder_pdf_to_png.py
   :language: python
   :linenos:

| The convert_pdf_to_png.py file is shown below.

.. literalinclude:: ../pdf_to_png_modules/convert_pdf_to_png.py
   :language: python
   :linenos:

| The magick_pdf_to_png.py module is shown below.

.. literalinclude:: ../pdf_to_png_modules/magick_pdf_to_png.py
   :language: python
   :linenos:

| The wand_pdf_to_png.py module is shown below.

.. literalinclude:: ../pdf_to_png_modules/wand_pdf_to_png.py
   :language: python
   :linenos:

----

VSCode LaTeX Workshop
-------------------------

| In VSCode, make sure that the LaTeX Workshop is installed.


LaTeX-workshop.LaTeX.tools json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Go to Preferences: Settings.
| Search for "LaTeX-workshop tools" or simply "LaTeX tools".
| Edit the tools json at: ``LaTeX-workshop.LaTeX.tools`` in the json file.
| Add the code block below to the tools json.
| Adjust the name value as preferred but it must be also adjusted in the recipe to be identical.
| Replace `Full_Path_folder` with the folder path for your python file.
| Put in the full path to the python script using `\\` as the folder delimiter.

.. code-block:: json

   {
      "name": "Python Script to Generate PNG",
      "command": "python",
      "args": [
            "Full_Path_folder\\LaTeX_pdf_to_png.py",
            "%DOCFILE%",
            "%OUTDIR%"
      ],
      "env": {}
   }



| The json code block defines a custom tool that can be used to convert a LaTeX document to a PNG image.
| Here is what each key in the object does:

   - `"name"`: name of the tool.
   - `"command"`: the command that will be executed when the tool is run. In this case, it is the Python interpreter.
   - `"args"`: These are the arguments that will be passed to the command when it is run. In this case, it is a list of three strings:

      - `"Full_Path_folder\\LaTeX_pdf_to_png.py"`: This is the path to the Python script that will be executed.
      - `"%DOCFILE%"`: This is a placeholder that will be replaced with the name of the LaTeX document file.
      - `"%OUTDIR%"`: This is a placeholder that will be replaced with the output directory for the PNG image. It is here in case it is needed for further actions in the python script that are yet to be scripted, such as copying the png to a pictures folder.

LaTeX-workshop.LaTeX.recipes json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Go to Preferences: Settings.
| Search for "LaTeX-workshop recipes" or simply "LaTeX recipes".
| Edit the recipe json at: ``LaTeX-workshop.LaTeX.recipes`` in the json file.

.. code-block:: json

   {
      "name": "PDF ➞ PNG",
      "tools": [
            "pdflatex",
            "Python Script to Generate PNG"
      ]
   }

| The json code block above is a custom tool called "PDF ➞ PNG" and it has two tools: "pdflatex" and "Python Script to Generate PNG".
| The tool is used to convert PDF files to PNG files.
| The pdflatex tool is used to generate the PDF file from the LaTeX source code.
| The Python script is then used to convert the PDF file to a PNG file.

| In View: Command Palette, enter "LaTeX workshop: Build with recipe" and choose "PDF ➞ PNG" to convert a tex file to pdf then to png.


Python LaTeX_pdf_to_png.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The python code to go in the python file ``LaTeX_pdf_to_png.py`` is below.
| Adjust the magick arguments to suit.

.. code-block:: python

   import sys
   import subprocess
import os

   tex_filename = sys.argv[1]
   pdf_path = f'{tex_filename}.pdf'
   png_path = f'{tex_filename}.png'

   subprocess.run(['magick', '-quiet', '-background', 'white', '-alpha', 'off', '-quality', '100', '-density', '600', pdf_path, png_path])


| ``sys.argv`` is a list in Python that contains the command-line arguments passed to the script. |
| ``tex_filename = sys.argv[1]`` assigns the first command-line argument passed to the script to the variable ``tex_filename``. From the tools json, the placeholder ``"%DOCFILE%"`` is the pdf file name that will be used to name the png file.

| This Python code uses the `subprocess.run()` method to execute the ImageMagick command line tool.
| The command line tool is used to convert a PDF file to a PNG file.
| Here is what each argument in the command does:

- `magick`: This is the ImageMagick command line tool.
- `-quiet`: suppresses all output except for errors and warnings.
- `-background white`: sets the background color of the output image to white.
- `-alpha off`: removes any transparency from the input image.
- `-quality 100`: sets the quality of the output image to 100%.
- `-density 600`: sets the resolution of the input PDF file to 600 DPI.
- `pdf_path`: is the path of the input PDF file.
- `png_path`: is the path of the output PNG file.




