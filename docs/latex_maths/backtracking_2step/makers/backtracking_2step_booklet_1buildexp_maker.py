from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_2step_booklet_template.tex"
texans_template_path = currfile_dir / "backtrack_2step_booklet_ans_template.tex"
tex_diagram_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_1buildexp_template.tex"
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



# % end modify values for backtracking
# tex_keys = ['stepAB','stepABrev','stepBC', 'stepBCrev', 'boxA','boxB', 'boxC', 'boxCrev, 'boxBrev', 'boxArev' ]
tex_keys_q = ["stepAB", "stepBC", "boxA"]


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
    num1 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 1st process \n")
    if num1.strip().isdigit():
        num1 = int(num1)
        if not num1 in [1, 2, 3, 4, 5]:
            num1 = 5  # random by default
    else:
        num1 = 5  # random by default
    #
    num2 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for the 2nd process \n")
    if num2.strip().isdigit():
        num2 = int(num2)
        if not num2 in [1, 2, 3, 4, 5]:
            num2 = 5  # random by default
    else:
        num2 = 5  # random by default
    #
    numq = input("Enter the number of questions from 1 to 100, with 20 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1,101):
            numq = 20  # random by default
    else:
        numq = 20  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix bt2Bk_bldexp_: \n")
    if not filename:
        filename = "1"  # "bt2Bk_bldexp_1st_q and bt2Bk_bldexp_1st_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"bt2Bk_bldexp_{filename}_q.tex"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"bt2Bk_bldexp_{filename}_ans.tex"


    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<cols>>
    # generate column text and column text for answers
    col1_text = ""
    col1_text_ans = ""
    for _ in range(1, numq + 1):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num1, num2)
        col1_text += img_tex
        col1_text_ans += img_tex_ans

    # Replace the <<cols>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<cols>>", col1_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<cols>>", col1_text_ans)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Write the answer tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the file to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
