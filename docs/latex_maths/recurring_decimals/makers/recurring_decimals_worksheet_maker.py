from pathlib import Path
import subprocess
import time
import recurring_decimals_functions as recdecf


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "recurring_decimals_worksheet_template.tex"
texans_template_path = currfile_dir / "recurring_decimals_worksheet_ans_template.tex"
tex_diagram_template_path = (
    currfile_dir / "recurring_decimals_worksheet_diagram_template.tex"
)
tex_diagram_ans_template_path = (
    currfile_dir / "recurring_decimals_worksheet_diagram_ans_template.tex"
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
            "pdfLaTeX",
            tex_path,
            "-output-directory",
            currfile_dir,
            "-aux-directory",
            aux_path,
        ],
        stdout=subprocess.PIPE,
    )


# tex_keys = ["numerator", "denominator", "nonrepeating", "repeating"]
tex_keys_q = ["numerator", "denominator"]


def make1_diagram(tex_diagram_template_txt, tex_diagram_template_txt_ans, num, denom):
    posttext = r"\vspace{12pt}"
    kv = recdecf.rec_dec_dict(num, denom)

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
    #
    numq = input("Enter the number of questions from 1 to 26 \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, 27):
            numq = 26  # 16 by default
    else:
        numq = 26  # 16 by default
    #
    #
    shuffle_bool = input("Enter T of F to shuffle the order \n").capitalize()
    if shuffle_bool == "T":
        shuffle_bool = True
    else:
        shuffle_bool = False
    #
    filename = input("Enter the base filename to be added to the prefix recdec_: \n")
    if not filename:
        filename = "1"  # "recdec_1_q and recdec_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"recdec_{filename}_q.tex"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"recdec_{filename}_ans.tex"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()
    with open(tex_diagram_ans_template_path, "r") as infile:
        tex_diagram_template_txt_ans = infile.read()

    num_denom_pairs_list = recdecf.get_num_denom_pairs_list(shuffle_bool)
    
    # <<cols>>
    # generate column text and column text for answers
    col1_text = ""
    col1_text_ans = ""
    rmax = numq + 1
    for i in range(1, rmax):
        num, denom = num_denom_pairs_list[i-1]
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, tex_diagram_template_txt_ans, num, denom)
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
