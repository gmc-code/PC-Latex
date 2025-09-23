from pathlib import Path
import magick_pdf_to_png
import wand_pdf_to_png

# paste in windows path to the raw string
raw_string =  r'C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC_latex\docs\latex_maths\grids\files\grids_isometic_horizontal.pdf'
# C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC_latex\docs\latex_maths\grids\files\grids_isometic_horizontal.pdf

forward_slash_string = raw_string.replace('\\', '/')
pdf_file_path = Path(forward_slash_string)
# parent_folder = pdf_file_path.parent
# file_path_without_extension = parent_folder / pdf_file_path.stem

# magick_pdf_to_png.pdf_to_png(pdf_file_path)

wand_pdf_to_png.pdf_to_png(pdf_file_path)
