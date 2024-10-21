from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_1step_worksheet_template.tex"
texans_template_path = currfile_dir / "backtrack_1step_worksheet_ans_template.tex"
tex_diagram_template_path = (
    currfile_dir / "backtrack_1step_worksheet_diagram_template.tex"
)


def convert_to_pdf(tex_path, currfile_dir, aux_path):
    """
    Converts a TeX file to PDF format using pdfLaTeX.

    Args:
        tex_path (str): The path to the TeX file.
        currfile_dir (str): The path to the directory where the TeX file is located.
        aux_path (str): The path to the directory where auxiliary files will be stored.

    Returns:
        subprocess.CompletedProcess: A subprocess.CompletedProcess object containing information about the completed process.

    Raises:
        FileNotFoundError: If the TeX file does not exist.
        subprocess.CalledProcessError: If pdfLaTeX returns a non-zero exit code.
    """
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


# tex_keys = ['stepAB','stepABrev','boxA','boxB','boxBrev', 'boxArev' ]
tex_keys_ans = ["stepAB", "boxA", "boxBrev"]


def make1_diagram(tex_diagram_template_txt, num):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{-2pt}"
    kv = btf.get_1step_process_dict(num)
    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )
    for key, value in kv.items():
        if key in tex_keys_ans:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", value
            )
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", ""
            )
    # return tex_diagram_template_txt
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


def main():
    num = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n")
    if num.strip().isdigit():
        num = int(num)
        if not num in [1, 2, 3, 4, 5]:
            num = 5  # random by default
    else:
        num = 5  # random by default
    filename = input("Enter the base filename to be added to the prefix bt1WS_: \n")
    if not filename:
        filename = "1"  # "bt1_1_q and bt1_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"bt1WS_{filename}_q.tex"
    pdf_path = currfile_dir / f"bt1WS_{filename}_q.pdf"
    png_path = currfile_dir / f"bt1WS_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"bt1WS_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"bt1WS_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"bt1WS_{filename}_ans.png"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<col1>>
    # generate column 1 text and column 1 text for answers
    col1_text = ""
    col1_text_ans = ""
    for i in range(1, 6):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
        col1_text += img_tex
        col1_text_ans += img_tex_ans

    # Replace the <<col1>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<col1>>", col1_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<col1>>", col1_text_ans)

    # generate column 2 text and column 2 text for answers
    col2_text = ""
    col2_text_ans = ""
    for i in range(6, 11):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
        col2_text += img_tex
        col2_text_ans += img_tex_ans

    # Replace the <<col2>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<col2>>", col2_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<col2>>", col2_text_ans)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Write the answer tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the PDFs to PNGs
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
