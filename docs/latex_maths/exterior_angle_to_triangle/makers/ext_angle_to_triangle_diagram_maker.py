from pathlib import Path
import subprocess
import time
import magick_pdf_to_png
import ext_angle_to_triangle_functions as aitf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "ext_angle_to_triangle_template.tex"
texans_template_path = currfile_dir / "ext_angle_to_triangle_template.tex"
tex_diagram_template_path = currfile_dir / "ext_angle_to_triangle_diagram_template.tex"


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


# % end modify values for angles in triangle
# replaced in q = ['angleCalcAValue', 'angleCalcBValue', 'angleCalcCValue', 'angleCalcExtBValue']
tex_keys_q = ['angleAValue', 'angleBValue', 'angleCValue', 'angleExtBValue',
              'sideCValue', 'sideDValue', 'rotationAngleValue',
              'angleALabel','angleBLabel', 'angleCLabel', 'angleDLabel', 'angleExtLabel']


def make1_diagram(tex_diagram_template_txt,):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = aitf.get_ext_angle_to_triangle_dict()
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
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    filename = input("Enter the base filename to be added to the prefix ext_angle_to_triangle_: \n")
    if not filename:
        filename = "1"  # "ext_angle_to_triangle_1_q and ext_angle_to_triangle_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"ext_angle_to_triangle_{filename}_q.tex"
    pdf_path = currfile_dir / f"ext_angle_to_triangle_{filename}_q.pdf"
    png_path = currfile_dir / f"ext_angle_to_triangle_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"ext_angle_to_triangle_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"ext_angle_to_triangle_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"ext_angle_to_triangle_{filename}_ans.png"

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
    diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt)
    # Replace the <<diagram>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<diagram>>", diagram_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<diagram>>", diagram_text_ans)
    # Write the question diagram tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)
    # Write the answer diagram tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the files to be created
    time.sleep(1)
    # convert to pdf
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # convert to png
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
