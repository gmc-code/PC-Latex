from pathlib import Path
import subprocess
import os
import time
import random
import os
import magick_pdf_to_png

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "number_lines_booklet_template.tex"
texans_template_path = currfile_dir / "number_lines_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "number_lines_neg20to0_booklet_diagram_template.tex"


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


def getprocess_dict(num, adjustment=0):
    if num is None or num == 6:
        num = random.randint(1, 5)
    match num:
        case 1:
            return go_right_dict("plus", adjustment)
        case 2:
            return go_right_dict("minus_neg", adjustment)
        case 3:
            return go_left_dict("minus", adjustment)
        case 4:
            return go_left_dict("minus_pos", adjustment)
        case 5:
            return go_left_dict("plus_neg", adjustment)


def val_in_list_exclude_zero(low, high):
    vals = list(range(low, high + 1))
    if 0 in vals:
        vals.remove(0)
    return random.choice(vals)


def go_right_dict(add_style, adjustment):
    # set points
    endval = val_in_list_exclude_zero(-7, 9)
    startval = val_in_list_exclude_zero(-9, endval - 2)
    endval += adjustment
    startval += adjustment
    changevaltxt = endval - startval
    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    if add_style == "plus":
        kv["changevaltxt"] = r"+" + str(changevaltxt)
    else:  # minus_neg
        kv["changevaltxt"] = r"-(" + str(-changevaltxt) + ")"
    kv["equtxt"] = f"{startval}{kv['changevaltxt']} = {endval}"
    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    if add_style == "plus":
        kv["changevaltxt_q"] = r"+\qgap"
        kv["equtxt_q"] = r"\qgap + \qgap = \qgap"
    else:  # minus_neg
        kv["changevaltxt_q"] = r"-(\qgap)"
        kv["equtxt_q"] = r"\qgap - (\qgap) = \qgap"
    return kv


def go_left_dict(sub_style, adjustment):
    # set points
    endval = val_in_list_exclude_zero(-9, 7)
    startval = val_in_list_exclude_zero(endval + 2, 9)
    endval += adjustment
    startval += adjustment
    changevaltxt = endval - startval
    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    if sub_style == "minus":
        kv["changevaltxt"] = r"-" + str(-changevaltxt)
    elif sub_style == "minus_pos":
        kv["changevaltxt"] = r"-(+" + str(-changevaltxt) + ")"
    else:  # plus_neg
        kv["changevaltxt"] = r"+(" + str(changevaltxt) + ")"
    kv["equtxt"] = f"{startval}{kv['changevaltxt']} = {endval}"
    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    if sub_style == "minus":
        kv["changevaltxt_q"] = r"-\qgap"
        kv["equtxt_q"] = r"\qgap - \qgap = \qgap"
    elif sub_style == "minus_pos":
        kv["changevaltxt_q"] = r"-(+\qgap)"
        kv["equtxt_q"] = r"\qgap - (+\qgap) = \qgap"
    else:  # plus_neg
        kv["changevaltxt_q"] = r"+(\qgap)"
        kv["equtxt_q"] = r"\qgap + (\qgap) = \qgap"
    return kv


kv_keys_ans = [
    "startval",
    "endval",
    "startvaltxt",
    "endvaltxt",
    "changevaltxt",
    "equtxt",
]
kv_keys_q = [
    "startval",
    "endval",
    "startvaltxt_q",
    "endvaltxt_q",
    "changevaltxt_q",
    "equtxt_q",
]


def trimkey(key):
    key = key.replace("_q", "")
    return key


def make1_diagram(tex_diagram_template_txt, num):
    posttext = r"\vspace{-2pt}"
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = getprocess_dict(num, adjustment=-10)
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
    num = input("Enter 1,2,3,4,5 or 6 for plus,minus_neg,minus,minus_pos,plus_neg,random \n")
    if num.strip().isdigit():
        num = int(num)
        if not num in [1, 2, 3, 4, 5, 6]:
            num = 6  # random by default
    else:
        num = 6  # random by default
    #
    numq = input("Enter the number of questions from 1 to 80, with 8 per page \n")
    if numq.strip().isdigit():
        numq = int(numq)
        if not numq in range(1, 81):
            numq = 16  # random by default
    else:
        numq = 16  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix nlBk_neg20to0_: \n")
    if not filename:
        filename = "1"  # "nlBk_1st_q and nlBk_1st_ans as default file"
    # set names of files that are made
    tex_output_path = currfile_dir / f"nlBk_neg20to0_{filename}_q.tex"
    pdf_path = currfile_dir / f"nlBk_neg20to0_{filename}_q.pdf"

    # answers
    tex_output_path_ans = currfile_dir / f"nlBk_neg20to0_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"nlBk_neg20to0_{filename}_ans.pdf"

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
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
        if i > 8 and i % 8 == 1:
            diagrams_text += headtext
            diagrams_text_ans += headtext
        diagrams_text += img_tex
        diagrams_text_ans += img_tex_ans

    # Replace the <<diagrams>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<diagrams>>", diagrams_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<diagrams>>", diagrams_text_ans)
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
