"""
Module to convert a pdf to a png using image magick
"""
from pathlib import Path
import subprocess
import os


def convert_pdf_to_png(pdf_path, png_path):
    """Called by pdf_to_png to Create a png from a pdf using 600 dpi and max quality
        Use the subprocess module to call Image Magick in the commandline

    Args:
        pdf_path (path object): full path to the pdf
        png_path (path object): full path to the png to be created

    magick args as a list:
        '-quiet' suppresses the warning in the terminal (that can be ignored), relating to colour profiles
        '-density','600' sets the dpi to 600
        '-quality','100' makes the best quality png
        '-alpha','off' is used here so all transparency is removed
    """
    result=subprocess.run(
        ['magick','-quiet','-density','1200',pdf_path,'-quality','100','-alpha','off',png_path]
    )



def pdf_to_png(pdf_file_path):
    """create a png from a pdf.
        png will be created with same file name in same folder as the pdf.

    Args:
        pdf_file_path (str): the full file path of a pdf.
    """

    forward_slash_string = pdf_file_path.replace("\\", "/")
    pdf_file_path = Path(forward_slash_string)

    parent_folder = Path(pdf_file_path).parent
    file_path_without_extension = parent_folder / pdf_file_path.stem
    png_path = f"{file_path_without_extension}.png"
    convert_pdf_to_png(pdf_file_path, png_path)
