from pathlib import Path
import subprocess
import time
import os
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_1step_booklet_template.tex"
texans_template_path = currfile_dir / "backtrack_1step_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "backtrack_1step_booklet_diagram_template.tex"


def merge_files(file1, file2, outputname):
    result = subprocess.run(["pdfunite", file1, file2, outputname])


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


# tex_keys = ['stepAB','stepABrev','boxA','boxB','boxBrev', 'boxArev' ]
tex_keys_q = ["stepAB", "boxA", "boxBrev"]


def make1_diagram(tex_diagram_template_txt, num):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{-2pt}"
    kv = btf.get_1step_process_dict(num)

    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<" + key + ">>", value)

    for key, value in kv.items():
        if key in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + key + ">>", value)
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + key + ">>", "")

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
    #
    numq = input("Enter the number of questions from 1 to 100 \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, 101):
            numq = 20  # random by default
    else:
        numq = 20  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix bt1Bk_: \n")
    if not filename:
        filename = "1"  # "bt1Bk_1st_q and bt1Bk_1st_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"bt1Bk_{filename}_q.tex"

    # answers
    tex_output_path_ans = currfile_dir / f"bt1Bk_{filename}_ans.tex"

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
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
        col_text += img_tex
        col_text_ans += img_tex_ans

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
