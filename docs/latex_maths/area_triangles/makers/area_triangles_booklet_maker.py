from pathlib import Path
import subprocess
import os
import time
import random
import magick_pdf_to_png
import area_triangles_functions as atf


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "area_triangles_booklet_template.tex"
texans_template_path = currfile_dir / "area_triangles_booklet_ans_template.tex"
tex_diagram_template_right_path = currfile_dir / "area_triangles_right_booklet_diagram_template.tex"
tex_diagram_template_acute_path = currfile_dir / "area_triangles_acute_booklet_diagram_template.tex"
tex_diagram_template_obtuse_path = currfile_dir / "area_triangles_obtuse_booklet_diagram_template.tex"


# list of sides so not repeated in max of 20
side_pairs_list = atf.get_side_pairs()
rotations_list = atf.get_rotations_shuffled()


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



################################################################################################


################################################################################################

def get_diagram_template_txt(num,tex_diagram_right_template_txt,tex_diagram_acute_template_txt,tex_diagram_obtuse_template_txt):
    match num:
        case 1:
            return tex_diagram_right_template_txt
        case 2:
            return tex_diagram_acute_template_txt
        case 3:
            return tex_diagram_obtuse_template_txt


def get_keys(num):
    tex_keys_q_right = ["calc_sidelength1", "calc_sidelength2", "sidelength1", "sidelength2", "rotation", "vA", "vB", "vC"]
    tex_keys_q_acute = ["calc_base", "calc_height", "leftoffset", "base", "height", "rotation", "vA", "vB", "vC", "vD"]
    tex_keys_q_obtuse = ["calc_base", "calc_height", "rightoffset", "base", "height", "rotation", "vA", "vB", "vC", "vD"]
    match num:
        case 1:
            return tex_keys_q_right
        case 2:
            return tex_keys_q_acute
        case 3:
            return tex_keys_q_obtuse


def get_kv(num,side_pairs, rotation):
    return atf.get_area_triangle_dict(num,side_pairs, rotation)

################################################################################################

def make1_diagram(tex_diagram_template_txt,tex_keys_q,kv):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\par\vspace{1cm}"  #  ~ \newline
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
        if not numq in range(1, 21):
            numq = 4  # random by default
    else:
        numq = 4  # random by default
    #
    num = input("Enter 1, 2, 3, or 4 for right,acute,obtuse,random \n")
    if num.strip().isdigit():
        num = int(num)
        if not num in [1, 2, 3, 4]:
            num = 4  # random by default
    else:
        num = 4  # random by default
    #
    filename = input(
        "Enter the base filename to be added to the prefix area_triangles_Bk_: \n"
    )
    if not filename:
        filename = "1"  # "area_triangles_Bk_1_q and area_triangles_Bk_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"area_triangles_Bk_{filename}_q.tex"
    pdf_path = currfile_dir / f"area_triangles_Bk_{filename}_q.pdf"

    # answers
    tex_output_path_ans = currfile_dir / f"area_triangles_Bk_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"area_triangles_Bk_{filename}_ans.pdf"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_right_path, "r") as infile:
        tex_diagram_right_template_txt = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_acute_path, "r") as infile:
        tex_diagram_acute_template_txt = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_obtuse_path, "r") as infile:
        tex_diagram_obtuse_template_txt = infile.read()

    # Generate the <<diagram>> replacement tex
    # diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt)

    # <<diagrams>>
    # generate diagrams text and text for answers
    diagrams_text = ""
    diagrams_text_ans = ""
    # add the headtext; disabled for now using r"" wno needed as numbers in minipage itself
    headtext = r""  # r"\pagebreak ~ \newline ~ \newline"
    for i in range(1, numq + 1):
        if num is None or num == 4:
            num_to_use = random.randint(1, 3)
        else:
            num_to_use = num
        side_pairs = side_pairs_list[i - 1]
        rotation = rotations_list[i - 1]
        #
        tex_keys_q = get_keys(num_to_use)
        kv = get_kv(num_to_use, side_pairs, rotation)
        tex_diagram_template_txt = get_diagram_template_txt(
            num_to_use, tex_diagram_right_template_txt,
            tex_diagram_acute_template_txt, tex_diagram_obtuse_template_txt)
        #
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt,
                                             tex_keys_q, kv)

        if i > 4 and i % 4 == 1:
            diagrams_text += headtext
            diagrams_text_ans += headtext
        diagrams_text += img_tex
        diagrams_text_ans += img_tex_ans

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
