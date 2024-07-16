"""
Module to convert a pdf to a png using the wand python module @GMC 2023
"""
from pathlib import Path
from wand.image import Image


def convert_pdf_to_png(pdf_path, png_path):
    """Called by pdf_to_png to create a png from a pdf using 600 dpi and max quality
        Use the Image class from wand.image module

    Args:
        pdf_path (path object): full path to the pdf
        png_path (path object): full path to the png to be created
    """
    with Image(filename=pdf_path, resolution=600) as img:
        img.format = "png"
        img.compression_quality = 99
        img.alpha_channel = "opaque"
        img.save(filename=png_path)


def pdf_to_png(pdf_file_path):
    """create a png from a pdf.
        png will be created with same file name in same folder as the pdf.

    Args:
        pdf_file_path (path object from pathlib): the full file path of a pdf.
    """
    parent_folder = pdf_file_path.parent
    file_path_without_extension = parent_folder / pdf_file_path.stem
    png_path = f"{file_path_without_extension}.png"
    convert_pdf_to_png(pdf_file_path, png_path)
