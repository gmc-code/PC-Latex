from pathlib import Path
import subprocess
import time
import magick_pdf_to_png
import invop_functions as iof


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "invop_2step_template.tex"
texans_template_path = currfile_dir / "invop_2step_template.tex"
tex_diagram_template_path = currfile_dir / "invop_2step_diagram_template.tex"


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
    # result = subprocess.run(
    #     [
    #         "pdflatex",
    #         tex_path,
    #         "-output-directory",
    #         currfile_dir,
    #         "-aux-directory",
    #         aux_path,
    #     ],
    #     stdout=subprocess.PIPE,
    # )
    result = subprocess.run(
        [
            "pdflatex",
            str(tex_path),
            "-output-directory", str(currfile_dir),
            "-aux-directory", str(aux_path),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        print(f"Error compiling {tex_path}:\n{result.stderr.decode()}")

# % end modify values for invop
#['line1_LHS', 'line2_LHS', 'line2_LHSq', 'line3_LHS', 'line4_LHS', 'line4_LHSq', 'line5_LHS', 'line1_RHS', 'line2_RHS', 'line2_RHSq', 'line3_RHS', 'line3_RHSq', 'line4_RHS', 'line4_RHSq', 'line5_RHS', 'line5_RHSq']
# get the full keys above then get those with q, then delete the q
tex_keys_q = ['line2_LHS', 'line4_LHS', 'line2_RHS', 'line3_RHS', 'line4_RHS', 'line5_RHS']


def make1_diagram(tex_diagram_template_txt, num1, num2):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = iof.get_2step_process_dict(num1, num2)
    # do ans sheet
    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )
    # do q sheet
    for key, value in kv.items():
        if key not in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", value
            )
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", kv[f'{key}q']
            )
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    num1 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 1st process \n")
    if num1.strip().isdigit():
        num1 = int(num1)
        if not num1 in [1, 2, 3, 4, 5]:
            num1 = 5  # random by default
    else:
        num1 = 5  # random by default
    #
    num2 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 2nd process \n")
    if num2.strip().isdigit():
        num2 = int(num2)
        if not num2 in [1, 2, 3, 4, 5]:
            num2 = 5  # random by default
    else:
        num2 = 5  # random by default
    #
    filename = input("Enter the base filename to be added to the prefix invop2_: \n")
    if not filename:
        filename = "1"  # "invop2_1_q and invop2_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"invop2_{filename}_q.tex"
    pdf_path = currfile_dir / f"invop2_{filename}_q.pdf"
    png_path = currfile_dir / f"invop2_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"invop2_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"invop2_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"invop2_{filename}_ans.png"

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
    diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt, num1, num2)
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
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
