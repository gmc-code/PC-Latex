from pathlib import Path
import subprocess
import time
import decimals_functions as decf

# import magick_pdf_to_png


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "add_sub_decimals_booklet_template.tex"
texans_template_path = currfile_dir / "add_sub_decimals_booklet_ans_template.tex"
tex_diagram_template_path = (
    currfile_dir / "add_sub_decimals_booklet_diagram_template.tex"
)
colbreak = "\columnbreak  % Break column after 30 questions \n"


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
            "pdfLaTeX",
            tex_path,
            "-output-directory",
            currfile_dir,
            "-aux-directory",
            aux_path,
        ],
        stdout=subprocess.PIPE,
    )


# tex_keys = ["num1", "num2", "process"]
tex_keys_q = ["answer"]

def make1_diagram(tex_diagram_template_txt, nump, numip, numdp):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = decf.get_add_sub_dec_dict(nump, numip, numdp)
    posttext = r"\vspace{-1pt}"

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
    tex_diagram_template_txt = tex_diagram_template_txt.replace("<<numip>>", str(numip))
    tex_diagram_template_txt = tex_diagram_template_txt.replace("<<numdp>>", str(numdp))
    tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<numip>>", str(numip))
    tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<numdp>>", str(numdp))
    # return tex_diagram_template_txt
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


def get_title(nump):
    match nump:
        case 1:
            return "Addition"
        case 2:
            return "Subtraction"
        case 3:
            return "Addition and subtraction"


def main():
    nump = input("Enter 1, 2, or 3 for +, -, random for the process \n")
    if nump.strip().isdigit():
        nump = int(nump)
        if not nump in [1, 2, 3]:
            nump = 3  # random by default
    else:
        nump = 3  # random by default
    # get title for part of heading indicating which process/es
    title = get_title(nump)
    #
    numip = input("Enter 1, 2, 3, or 4 for the number of places before the decimal point: \n")
    if numip.strip().isdigit():
        numip = int(numip)
        if not numip in [1, 2, 3, 4, 5]:
            numip = 1  # 1 by default
    else:
        numip = 1  # 1 by default
    #
    numdp = input("Enter 1, 2, 3, 4, or 5 for the number of decimal places: \n")
    if numdp.strip().isdigit():
        numdp = int(numdp)
        if not numdp in [1, 2, 3, 4, 5]:
            numdp = 1  # 1 by default
    else:
        numdp = 1  # 1 by default
    #
    #
    numq = input("Enter the number of questions from 1 to 100, with 25 per page: \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, 101):
            numq = 25  # 25 by default
    else:
        numq = 25  # 25 by default
    #
    filename = input("Enter the base filename to be added to the prefix asd_: \n")
    if not filename:
        filename = "1"  # "asd_1_q and asd_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"asdBK_{filename}_q.tex"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"asdBK_{filename}_ans.tex"

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
    rmax = numq + 1
    for i in range(1, rmax):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, nump, numip, numdp)
        col1_text += img_tex
        col1_text_ans += img_tex_ans
        if i % 25 == 0 and i > 0 and i != numq:
            col1_text += colbreak
            col1_text_ans += colbreak


    # Replace the <<title>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<title>>", title)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<title>>", title)
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
