from pathlib import Path
import subprocess
import os
import time
# import magick_pdf_to_png
import check_solution_functions as chsolf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "check_solution_booklet_template.tex"
texans_template_path = currfile_dir / "check_solution_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "check_solution_booklet_diagram_template.tex"

q_per_column = 5
q_per_page = q_per_column * 2
max_q = 100


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


# % end modify values for check_solution
# tex_keys = []
tex_keys_q = ["LHS", "LHSsub", "LHSval", "RHS", "side_equality", "is_a_sol"]


def make1_diagram(
    tex_diagram_template_txt,
    num1,
):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = chsolf.get_1step_process_dict(num1)
    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<" + key + ">>", value)
    for key, value in kv.items():
        if key not in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + key + ">>", value)
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + key + ">>", kv[f"{key}q"])
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
    numq = input("Enter the number of questions from 1 to 100; with 10 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, max_q + 1):
            numq = max_q  # max
    else:
        numq = q_per_page  # by default fits on one page
    #
    filename = input("Enter the base filename to be added to the prefix check_solution_Bk_: \n")
    if not filename:
        filename = "1"  # "check_solution_Bk_1_q and check_solution_Bk_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"check_solution_Bk_{filename}_q.tex"
    pdf_path = currfile_dir / f"check_solution_Bk_{filename}_q.pdf"

    # answers
    tex_output_path_ans = currfile_dir / f"check_solution_Bk_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"check_solution_Bk_{filename}_ans.pdf"

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
    headtext_col = r"""\columnbreak
    """
    headtext_page = r"""\newpage
    """
    # headtext_page = r'''\newpage ~ \newline ~ \newline# '''

    for i in range(1, numq + 1):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num1)
        diagrams_text += img_tex
        diagrams_text_ans += img_tex_ans
        if i % q_per_page == 0 and numq + 1 > i:
            diagrams_text += headtext_page
            diagrams_text_ans += headtext_page
        elif i % q_per_column == 0 and i > 1 and numq + 1 > i:
            diagrams_text += headtext_col
            diagrams_text_ans += headtext_col

    # Replace the <<diagrams>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<diagrams>>", diagrams_text_ans)
    # Replace the <<chsol_filename>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<chsol_filename>>", filename)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<chsol_filename>>", filename)


    # Write the question diagrams tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)
    # Write the answer diagrams tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the files to be created
    time.sleep(1)
    # convert to pdf
    convert_to_pdf(tex_output_path, currfile_dir)
    convert_to_pdf(tex_output_path_ans, currfile_dir)

    # Wait for the files to be created
    # time.sleep(1)
    # convert to png
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
