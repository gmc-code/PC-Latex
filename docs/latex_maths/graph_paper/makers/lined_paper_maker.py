from pathlib import Path
import subprocess
import os
import time
import lined_paper_functions as lpf

currfile_dir = Path(__file__).parent
tex_paper_template_path = currfile_dir / "lined_paper_template.tex"
tex_page_template_path = currfile_dir / "lined_page_template.tex"


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

#####################################################################################


def main():
    num = input(
        "Enter the number of lines from 1 to 26; or 0 for full page \n")
    if num.strip().isdigit():
        num = int(num)
        if not num in range(1, 27):
            num = 0
    else:
        num = 0
    #
    filename = input(
        "Enter the base filename to be added to the prefix lined_paper_: \n")
    if not filename:
        filename = "1"
    # set names of files that are made
    tex_output_path = currfile_dir / f"lined_paper_{filename}.tex"

    if num == 0:
        tex_template_path = tex_page_template_path
    else:
        tex_template_path = tex_paper_template_path

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()

    # <<diagrams>>
    if num == 0:
        # full page
        diagrams_text = lpf.get_lined_page_diagram(num)
        # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
        tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
    else:
        diagrams_text = lpf.get_lined_paper_diagram(num)
        # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
        tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
        #
        paperheight = lpf.get_lined_paper_height(num)
        # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
        tex_template_txt = tex_template_txt.replace("<<paperheight>>", paperheight)

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
