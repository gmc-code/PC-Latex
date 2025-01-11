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
    col_text = ""
    col_text_ans = ""
    for i in range(1, numq + 1):
        num, denom = num_denom_pairs_list[i-1]
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, tex_diagram_template_txt_ans, num, denom)
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
