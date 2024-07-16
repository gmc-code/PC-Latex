from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_2step_worksheet_template.tex"
texans_template_path = currfile_dir / "backtrack_2step_worksheet_ans_template.tex"
tex_diagram_template_path = (
    currfile_dir / "backtrack_2step_worksheet_diagram_template.tex"
)


def convert_to_pdf(tex_path, currfile_dir, aux_path):
    result = subprocess.run(
        [
            "pdfLaTeX",
            tex_path,
            "-output-directory",
            currfile_dir,
            "-aux-directory",
            aux_path,
        ],
        stdout=subprocess.PIPE,
    )


# % end modify values for backtracking
# tex_keys = ['stepAB','stepABrev','stepBC', 'stepBCrev', boxA','boxB', 'boxC', 'boxCrev, 'boxBrev', 'boxArev' ]
tex_keys_q = ["stepAB", "stepBC", "boxA", "boxCrev"]


def make1_diagram(tex_diagram_template_txt, num1, num2):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{-2pt}"
    kv = btf.get_2step_process_dict(num1, num2)
    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )
    for key, value in kv.items():
        if key in tex_keys_q:
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
    num1 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 1st process \n")
    if num1.strip().isdigit():
        num1 = int(num1)
        if not num1 in [1, 2, 3, 4, 5]:
            num1 = 5  # random by default
    else:
        num1 = 5  # random by default
    num2 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 2nd process \n")
    if num2.strip().isdigit():
        num2 = int(num2)
        if not num2 in [1, 2, 3, 4, 5]:
            num2 = 5  # random by default
    else:
        num2 = 5  # random by default
    filename = input("Enter the base filename to be added to the prefix bt2WS_: \n")
    if not filename:
        filename = "bt2WS_1st"  # "bt2WS_1st_q and bt2WS_1st_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"bt2WS_{filename}_q.tex"
    pdf_path = currfile_dir / f"bt2WS_{filename}_q.pdf"
    png_path = currfile_dir / f"bt2WS_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"bt2WS_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"bt2WS_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"bt2WS_{filename}_ans.png"

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
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num1, num2)
        col1_text += img_tex
        col1_text_ans += img_tex_ans

    # Replace the <<col1>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<col1>>", col1_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<col1>>", col1_text_ans)

    # generate column 2 text and column 2 text for answers
    col2_text = ""
    col2_text_ans = ""
    for i in range(6, 11):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num1, num2)
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
