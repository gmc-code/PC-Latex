from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_2step_booklet_template.tex"
tex_diagram_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_blank_template.tex"
)


def convert_to_pdf(tex_path, currfile_dir, aux_path):
    result = subprocess.run(
        [
            "pdflatex",
            tex_path,
            "-output-directory",
            currfile_dir,
            "-aux-directory",
            aux_path,
        ],
        stdout=subprocess.PIPE,
    )


def main():
    numq = input("Enter the number of questions from 1 to 100, with 10 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1,101):
            numq = 20  # random by default
    else:
        numq = 20  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix bt2Bk_: \n")
    if not filename:
        filename = "blnk"  # "bt2Bk_blnk as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"bt2Bk_{filename}.tex"
    aux_path = currfile_dir / "temp"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<cols>>
    # generate column text and column text for answers
    col1_text = ""
    for _ in range(1, numq + 1):
        col1_text += tex_diagram_template_txt

    # Replace the <<cols>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<cols>>", col1_text)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)


    # Wait for the file to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
