from pathlib import Path
import subprocess
import os
import time

import random
import magick_pdf_to_png
import decimals_functions as decf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "decimals_booklet_template.tex"
texans_template_path = currfile_dir / "decimals_booklet_ans_template.tex"
tex_diagram_template_path = (
    currfile_dir / "decimals_booklet_diagram_template.tex"
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


# tex_keys = ["num1", "num2", "process"]
tex_keys_q = ["answer"]


def make1_diagram(tex_diagram_template_txt, num, numdp):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{-2pt}"
    kv = decf.get_dec_dict(num, numdp)

    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )

    for key, value in kv.items():
        if key in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", ""
            )
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", value
            )

    # return tex_diagram_template_txt
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


def get_title(num):
    match num:
        case 1:
            return "Addition"
        case 2:
            return "Subtraction"
        case 3:
            return "Addition and subtraction"


def main():
    num = input("Enter 1, 2, or 3 for +, -, random for the process \n")
    if num.strip().isdigit():
        num = int(num)
        if not num in [1, 2, 3]:
            num = 3  # random by default
    else:
        num = 3  # random by default
    # egt title for part of heading indicating which process/es
    title = get_title(num)
    #
    numdp = input("Enter 1, 2 or 3 for the number of decimal places \n")
    if numdp.strip().isdigit():
        numdp = int(numdp)
        if not numdp in [1, 2, 3]:
            numdp = 1  # random by default
    else:
        numdp = 1  # random by default
    #
    #
    numq = input("Enter the number of questions from 1 to 100 \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, 101):
            numq = 20  # random by default
    else:
        numq = 20  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix asd_: \n")
    if not filename:
        filename = "1"  # "asd_1_q and asd_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"asd_{filename}_q.tex"
    # answers
    tex_output_path_ans = currfile_dir / f"asd_{filename}_ans.tex"

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
    col_text = ""
    col_text_ans = ""
    for _ in range(1, numq + 1):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num, numdp)
        col_text += img_tex
        col_text_ans += img_tex_ans

    # Replace the <<title>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<title>>", title)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<title>>", title)
    # Replace the <<cols>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<cols>>", col_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<cols>>", col_text_ans)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Write the answer tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the file to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir)
    convert_to_pdf(tex_output_path_ans, currfile_dir)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
