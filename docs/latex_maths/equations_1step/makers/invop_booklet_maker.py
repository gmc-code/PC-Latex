from pathlib import Path
import subprocess
import time
# import magick_pdf_to_png
import invop_functions as iof

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "invop_booklet_template.tex"
texans_template_path = currfile_dir / "invop_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "invop_booklet_diagram_template.tex"

q_per_column = 8
q_per_page = q_per_column * 2
max_q = 96

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


# % end modify values for invop
# tex_keys = ['ans_force_l','ans_force_e','ans_dist_l', 'ans_dist_e', 'effort_vector','fulc_c', 'fulc_l', 'fulc_r' ]
tex_keys_q = ['line1_LHS', 'line1_RHS', 'line2_LHSq', 'line2_RHSq', 'line3_LHS', 'line3_RHSq']



def make1_diagram(tex_diagram_template_txt, num1,):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = iof.get_1step_process_dict(num1)
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
                "<<" + key + ">>", kv[f'{key}q']
            )
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    num1 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n")
    if num1.strip().isdigit():
        num1 = int(num1)
        if not num1 in [1, 2, 3, 4, 5]:
            num1 = 5  # random by default
    else:
        num1 = 5  # random by default
    #
    numq = input("Enter the number of questions from 1 to 96, with 16 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, max_q + 1):
            numq = max_q  # max
    else:
        numq = q_per_page  # by default fits on one page
    #
    filename = input(
        "Enter the base filename to be added to the prefix invop_Bk_: \n")
    if not filename:
        filename = "1"  # "invop_Bk_1_q and invop_Bk_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"invop_Bk_{filename}_q.tex"
    pdf_path = currfile_dir / f"invop_Bk_{filename}_q.pdf"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"invop_Bk_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"invop_Bk_{filename}_ans.pdf"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # Generate the <<diagram>> replacement tex
    # diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt, num1)

    # <<diagrams>>
    # generate diagrams text and text for answers
    diagrams_text = ""
    diagrams_text_ans = ""
    # add the headtext
    # must have no space in \end{minipage}\columnbreak for column break to occur at correct place.
    headtext_col = r'''\columnbreak
    '''
    headtext_page = r'''\newpage
    '''
    # headtext_page = r'''\newpage ~ \newline ~ \newline
    # '''
    rmax = numq + 1

    for i in range(1, rmax):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num1)
        diagrams_text += img_tex
        diagrams_text_ans += img_tex_ans
        if i % q_per_page == 0 and rmax > i:
            diagrams_text += headtext_page
            diagrams_text_ans += headtext_page
        elif i % q_per_column == 0 and i > 1 and rmax > i:
            diagrams_text += headtext_col
            diagrams_text_ans += headtext_col

    # Replace the <<diagrams>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
    tex_template_txt_ans = tex_template_txt_ans.replace(
        "<<diagrams>>", diagrams_text_ans)
    # Write the question diagrams tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)
    # Write the answer diagrams tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the files to be created
    time.sleep(1)
    # convert to pdf
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)

    # Wait for the files to be created
    # time.sleep(1)
    # convert to png
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
