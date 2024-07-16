from pathlib import Path
import subprocess
import time
import magick_pdf_to_png
import angles_in_rt_triangle_functions as aitf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "angles_in_rt_triangle_booklet_template.tex"
texans_template_path = currfile_dir / "angles_in_rt_triangle_booklet_ans_template.tex"
tex_diagram_template_path = currfile_dir / "angles_in_rt_triangle_booklet_diagram_template.tex"


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


# % end modify values for angles in triangle 
# tex_keys_q = ['angleCalcAValue', 'angleCalcBValue', 'angleCalcCValue', 'angleCalcBCValue']
tex_keys_q = ['angleAValue', 'angleBValue', 'angleCValue', 'angleBCValue', 
              'sideCValue', 'rotationAngleValue', 'angleALabel','angleBLabel', 'angleCLabel']


def make1_diagram(tex_diagram_template_txt):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{1cm}"  #  ~ \newline
    kv = aitf.get_angles_in_rt_triangle_dict()
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
                "<<" + key + ">>", "\dotuline{~~~~~~~}"  # non breaking spaces for gaps
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
    
    filename = input("Enter the base filename to be added to the prefix angles_in_triangle_Bk_: \n")
    if not filename:
        filename = "1"  # "angles_in_triangle_Bk_1_q and angles_in_triangle_Bk_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"angles_in_rt_triangle_Bk_{filename}_q.tex"
    pdf_path = currfile_dir / f"angles_in_rt_triangle_Bk_{filename}_q.pdf"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"angles_in_rt_triangle_Bk_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"angles_in_rt_triangle_Bk_{filename}_ans.pdf"
  
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
    rmax = numq + 1
    for i in range(1, rmax):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt)
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
