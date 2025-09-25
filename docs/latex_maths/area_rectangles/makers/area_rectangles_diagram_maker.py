from pathlib import Path
import subprocess
import os
import time
import magick_pdf_to_png
import area_rectangles_functions as arf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "area_rectangles_template.tex"
texans_template_path = currfile_dir / "area_rectangles_template.tex"
tex_diagram_template_path = currfile_dir / "area_rectangles_diagram_template.tex"



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


#
# calcside_value1, calcside_value2, calcarea_value
tex_keys_q = ["calc_sidelength1", "calc_sidelength2", "sidelength1", "sidelength2", "rotation", "vA", "vB", "vC", "vD"]


def make1_diagram(
    tex_diagram_template_txt,
):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = arf.get_area_rectangles_dict()
    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<" + key + ">>", value)
    for key, value in kv.items():
        if key in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + key + ">>", value)
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace("<<" + key + ">>", "\\dotuline{~~~~~~~}")  # non breaking spaces for gaps
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    filename = input("Enter the base filename to be added to the prefix area_rectangles_: \n")
    if not filename:
        filename = "1"  # "area_rectangles_1_q and area_rectangles_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"area_rectangles_{filename}_q.tex"
    pdf_path = currfile_dir / f"area_rectangles_{filename}_q.pdf"
    png_path = currfile_dir / f"area_rectangles_{filename}_q.png"

    # answers
    tex_output_path_ans = currfile_dir / f"area_rectangles_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"area_rectangles_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"area_rectangles_{filename}_ans.png"

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
    convert_to_pdf(tex_output_path, currfile_dir)
    convert_to_pdf(tex_output_path_ans, currfile_dir)

    # Wait for the files to be created
    time.sleep(1)
    # convert to png
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
