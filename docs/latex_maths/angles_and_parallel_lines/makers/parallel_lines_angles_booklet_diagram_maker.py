from pathlib import Path
import subprocess
import os
import time
import magick_pdf_to_png
import parallel_lines_angles_functions as plaf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "parallel_lines_angles_booklet_template.tex"
texans_template_path = currfile_dir / "parallel_lines_angles_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "parallel_lines_angles_booklet_diagram_template.tex"


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
        # if tex_path.exists():
        #     os.remove(tex_path)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


# % keys for questions, omit ans keys
# tex_keys_q = ['aval', 'bval', 'cval', 'dval', 'eval', 'fval', 'gval', 'hval', 'angle_to_find_value']
tex_keys_q = ["rotationAngle", "parIstartx", "parIstarty", "parIendx", "parIendy",
              "parIIstartx", "parIIstarty", "parIIendx", "parIIendy",
              "transstartx", "transstarty", "transendx", "transendy",
              "anglestext",
              'alabel', 'blabel', 'clabel', 'dlabel', 'elabel', 'flabel', 'glabel', 'hlabel', 'angle_to_find'
              ]

def make1_diagram(tex_diagram_template_txt, num):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{1cm}"  #  ~ \newline
    kv = plaf.choose_parallel_lines_angles_dict(num)
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
                "<<" + key + ">>", "\\dotuline{~~~~~~~}"  # non breaking spaces for gaps
            )
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


def main():
    numq = input("Enter the number of questions from 1 to 20 \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1,21):
            numq = 4  # random by default
    else:
        numq = 4  # random by default
    #
    num = input("Enter 1, 2, 3, 4, 5, 6, or 7 for corresponding, alternate, cointerior, verticall_opposite, consecutive_exterior, alternate_exterior, random \n")
    if num.strip().isdigit():
        num = int(num)
        if not num in [1, 2, 3, 4, 5, 6]:
            num = 7  # random by default
    else:
        num = 7  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix pla_Bk_: \n")
    if not filename:
        filename = "1"  # "parallel_lines_angles_Bk_1_q and parallel_lines_angles_Bk_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"pla_Bk_{filename}_q.tex"
    pdf_path = currfile_dir / f"pla_Bk_{filename}_q.pdf"

    # answers
    tex_output_path_ans = currfile_dir / f"pla_Bk_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"pla_Bk_{filename}_ans.pdf"

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
    # diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt)

    # <<diagrams>>
    # generate diagrams text and text for answers
    diagrams_text = ""
    diagrams_text_ans = ""
    # add the headtext; disabled for now using r"" wno needed as numbers in minipage itself
    headtext = r""  # r"\pagebreak ~ \newline ~ \newline"

    for i in range(1, numq + 1):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
        if i > 4 and i % 4 == 1:
            diagrams_text += headtext
            diagrams_text_ans += headtext
        diagrams_text += img_tex
        diagrams_text_ans += img_tex_ans

    # Replace the <<diagrams>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<diagrams>>", diagrams_text_ans)
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
