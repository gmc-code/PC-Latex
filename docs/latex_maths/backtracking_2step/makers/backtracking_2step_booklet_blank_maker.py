from pathlib import Path
import subprocess
import os
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_2step_booklet_template.tex"
tex_diagram_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_blank_template.tex"
)


def convert_to_pdf(tex_path, outputdir):
    tex_path = Path(tex_path).resolve()
    outputdir = Path(outputdir).resolve()
    # for testing
    # print(f"tex_path: {tex_path}")
    # print(f"outputdir: {outputdir}")
    try:
        # Generate the PDF
        subprocess.run(["latexmk", "-pdf", "-outdir=" + str(outputdir), str(tex_path)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # # Clean auxiliary files after successful PDF generation
        subprocess.run(["latexmk", "-c", "-outdir=" + str(outputdir), str(tex_path)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # for hosted remove stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL for debugging any errors
        # Remove the .tex file manually
        if tex_path.exists():
            os.remove(tex_path)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


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


    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<diagrams>>
    # generate column text and column text for answers
    diagram_text = ""
    for _ in range(1, numq + 1):
        diagram_text += tex_diagram_template_txt

    # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagram_text)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)


    # Wait for the file to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
