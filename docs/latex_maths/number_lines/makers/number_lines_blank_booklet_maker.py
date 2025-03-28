from pathlib import Path
import subprocess
import os
import time


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "number_lines_booklet_template.tex"
tex_diagram_template_path = currfile_dir / "number_lines_blank_booklet_diagram_template.tex"


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
        # if tex_path.exists():
        #     os.remove(tex_path)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def make1_diagram(tex_diagram_template_txt):
    posttext = r"\vspace{1pt}"
    return tex_diagram_template_txt + posttext

def main():
    numq = input("Enter the number of questions from 1 to 80, with 8 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1,81):
            numq = 16  # random by default
    else:
        numq = 16  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix nlBk_blank_: \n")
    if not filename:
        filename = "1"
    # set names of files that are made
    tex_output_path = currfile_dir / f"nlBk_blank_{filename}.tex"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()

    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<diagrams>>
    # generate diagrams text and text for answers
    diagrams_text = ""
    # add the headtext
    headtext = r"\pagebreak ~ \newline ~ \newline"
    for i in range(1, numq + 1):
        img_tex = make1_diagram(tex_diagram_template_txt)
        if i > 8 and i % 8 == 1:
            diagrams_text += headtext
        diagrams_text += img_tex

    # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Wait for the file to be created
    time.sleep(2)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir)



if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
