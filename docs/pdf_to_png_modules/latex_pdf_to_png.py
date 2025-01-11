"""
Script used by LaTeX workshop using tools/recipe @GMC 2023
"""
import sys
import subprocess

tex_filename = sys.argv[1]
# tex_file_directory = sys.argv[2]
pdf_path = f'{tex_filename}.pdf'
png_path = f'{tex_filename}.png'

# this also works:
# subprocess.run(f'magick convert -quiet -background white -alpha off -quality 100 -density 600 {tex_filename}.pdf {tex_filename}.png')

subprocess.run(['magick','-quiet', '-background', 'white', '-alpha', 'off', '-quality', '100', '-density', '600', pdf_path, png_path])

