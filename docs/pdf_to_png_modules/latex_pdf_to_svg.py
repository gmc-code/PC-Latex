"""
Script used by LaTeX workshop using tools/recipe @GMC 2023
"""
import sys
import subprocess
import os

tex_filename = sys.argv[1]
# tex_file_directory = sys.argv[2]
pdf_path = f"{tex_filename}.pdf"
svg_path = f"{tex_filename}.svg"

# this also works:

subprocess.run(["inkscape", "-z", "-l", pdf_path, svg_path])
