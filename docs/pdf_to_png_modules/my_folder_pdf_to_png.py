"""
Paste in a full folder path to convert pdfs therewithin to pngs @GMC 2023
"""
import pathlib

import magick_pdf_to_png
import wand_pdf_to_png


def get_pdf_files(pdf_folder_path):
    pdf_files = []
    for file in pathlib.Path(pdf_folder_path).iterdir():
        if file.is_file() and file.suffix == ".pdf":
            pdf_files.append(file.name)
    return pdf_files


def convert_folder(pdf_folder_path, pdfs_files):
    for filename in pdfs_files:
        pdf_file_path = pdf_folder_path / filename
        magick_pdf_to_png.pdf_to_png(pdf_file_path)
        # comment out wand or magick
        # wand_pdf_to_png.pdf_to_png(pdf_file_path)


# a raw r string is used since backslashes are normally escape characters
# paste in windows pdf full file path
pasted_folder_path = r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC_latex\docs\latex_science\ray_tracing\files\New folder"

pdf_folder_path = pathlib.PureWindowsPath(pasted_folder_path)
pdfs_files = get_pdf_files(pdf_folder_path)
convert_folder(pdf_folder_path, pdfs_files)
