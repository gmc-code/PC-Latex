from pathlib import Path
import subprocess
import os
import time
import random
import os
import magick_pdf_to_png
import number_lines_2step_functions as nlf


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "number_lines_2step_booklet_template.tex"
texans_template_path = currfile_dir / "number_lines_2step_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "number_lines_2step_booklet_diagram_template.tex"

# gaps = "\qgap"
# gaps = "\dotuline{\phantom{X}}"
gaps = "\raisebox{-2pt}{\dotuline{\phantom{X}}"

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


kv_keys_ans = ["startval", "midval", "endval", "startvaltxt", "midvaltxt", "endvaltxt", "firstjumptxt", "secondjumptxt", "equtxt"]
kv_keys_q = ["startval", "midval", "endval", "startvaltxt_q", "midvaltxt_q", "endvaltxt_q", "firstjumptxt_q", "secondjumptxt_q", "equtxt_q"]


def trimkey(key):
    key = key.replace("_q", "")
    return key


def make1_diagram(tex_diagram_template_txt, num1, num2):
    posttext = r"\vspace{-2pt}"
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = nlf.get_2step_process_dict(num1, num2)
    for key, value in kv.items():
        # show answers
        if key in kv_keys_ans:
            tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<" + key + ">>", value)
    for key, value in kv.items():
        # don't show answers, use ___ for gaps
        if key in kv_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + trimkey(key) + ">>", value)
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


def main():
    num1 = input(
        "Enter 1,2,3,4,5 or 6 for first step: plus,minus_neg,minus,minus_pos,plus_neg,random \n"
    )
    if num1.strip().isdigit():
        num1 = int(num1)
        if not num1 in [1, 2, 3, 4, 5, 6]:
            num1 = 6  # random by default
    else:
        num1 = 6  # random by default
    #
    num2 = input(
        "Enter 1,2,3,4,5 or 6 for second step: plus,minus_neg,minus,minus_pos,plus_neg,random \n"
    )
    if num2.strip().isdigit():
        num2 = int(num2)
        if not num2 in [1, 2, 3, 4, 5, 6]:
            num2 = 6  # random by default
    else:
        num2 = 6  # random by default
    #
    numq = input(
        "Enter the number of questions from 1 to 80, with 8 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, 81):
            numq = 16  # random by default
    else:
        numq = 16  # random by default
    #
    filename = input(
        "Enter the base filename to be added to the prefix nlBk2_: \n")
    if not filename:
        filename = "1"  # "nlBk_1st_q and nlBk_1st_ans as default file"
    # set names of files that are made
    tex_output_path = currfile_dir / f"nlBk2_{filename}_q.tex"
    pdf_path = currfile_dir / f"nlBk2_{filename}_q.pdf"

    # answers
    tex_output_path_ans = currfile_dir / f"nlBk2_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"nlBk2_{filename}_ans.pdf"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<diagrams>>
    # generate diagrams text and text for answers
    diagrams_text = ""
    diagrams_text_ans = ""
    # add the headtext
    headtext = r"\pagebreak ~ \newline ~ \newline"
    for i in range(1, numq + 1):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num1,
                                             num2)
        if i > 8 and i % 8 == 1:
            diagrams_text += headtext
            diagrams_text_ans += headtext
        diagrams_text += img_tex
        diagrams_text_ans += img_tex_ans

    # Replace the <<title>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<title>>", title)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<title>>", title)

    # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
    tex_template_txt_ans = tex_template_txt_ans.replace(
        "<<diagrams>>", diagrams_text_ans)
    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Write the answer tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the file to be created
    time.sleep(2)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir)
    convert_to_pdf(tex_output_path_ans, currfile_dir)

    # # don't convert to images
    # time.sleep(1)
    # # Convert the PDFs to PNGs
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path,png_path)
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans,png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
