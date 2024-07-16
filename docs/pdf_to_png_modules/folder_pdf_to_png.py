"""
Paste in a full folder path to convert pdfs therewithin to pngs @GMC 2023
"""
from pathlib import Path
from tkinter import filedialog


import magick_pdf_to_png
import wand_pdf_to_png


def main():
    currfile_dir = Path(__file__).parent
    pdf_dir = filedialog.askdirectory(initialdir=currfile_dir)
    if pdf_dir == "":
        print("Exited, by clicking Cancel")
        return


    for pdf_file_path in Path(pdf_dir).glob("*.pdf"):
        print(pdf_file_path)
        magick_pdf_to_png.pdf_to_png(pdf_file_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
