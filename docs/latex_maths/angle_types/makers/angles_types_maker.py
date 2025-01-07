from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "angle_types_q_template.tex"
texans_template_path = currfile_dir / "angle_types_ans_template.tex"


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


def random_angles():
    text = "{acuteangle, rightangle, obtuseangle, straightangle, reflexangle, revolution}"
    # Step 1: Convert the text string into a list of words
    words = text.strip("{}").split(", ")
    # Step 2: Shuffle the list of words
    random.shuffle(words)
    # Step 3: Join the shuffled list of words back into a text string
    shuffled_text = "{" + ", ".join(words) + "}"
    return shuffled_text


def main():

    filename = input("Enter the filename suffix to be added to the prefix angle_types_: \n")
    if not filename:
        filename = "1"  #  angle_types_1_q as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"angle_types_{filename}_q.tex"
    pdf_path = currfile_dir / f"angle_types_{filename}_q.pdf"
    png_path = currfile_dir / f"angle_types_{filename}_q.png"

    # answers
    tex_output_path_ans = currfile_dir / f"angle_types_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"angle_types_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"angle_types_{filename}_ans.png"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()

    # Generate the <<diagram>> replacement tex
    new_diagram_list = random_angles()
    # Replace the <<diagram>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<macro_order>>", new_diagram_list)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<macro_order>>", new_diagram_list)
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
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
