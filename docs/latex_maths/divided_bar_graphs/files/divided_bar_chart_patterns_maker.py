from pathlib import Path
import subprocess
import os
from tkinter import filedialog
import time
import magick_pdf_to_png

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "divided_bar_chart_patterns_template.tex"


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


def get_list_from_str(data_string):
    if ", " in data_string:
        data_list = data_string.split(", ")
    elif "," in data_string:
        data_list = data_string.split(",")
    else:
        data_list = data_string.split(" ")
    return data_list


def get_list_nums_from_str(num_string_list):
    have_dec = any("." in s for s in num_string_list)
    if have_dec:
        num_list = [float(n) for n in num_string_list]
    else:
        num_list = [int(n) for n in num_string_list]
    return num_list


def get_substrings_from_string(data_string):
    new_string = ""
    for s in data_string.split(","):
        new_string += f'"{s}",'
    new_string = new_string[:-1]
    return new_string


def get_file_data(filename):
    # open the text file and read the numbers
    with open(filename) as f:
        # read the first line and store it in a variable
        plot_title = f.readline().strip()
        # read the second line and store it in a variable
        numbers_string = f.readline().strip()
        # read the third line and store it in a variable
        numbers_labels = f.readline().strip()
    #
    numbers_list = get_list_from_str(numbers_string)
    numbers_labels = get_substrings_from_string(numbers_labels)
    # process numbers
    numbers_loop_max = str(len(numbers_list) - 1)
    numbers_list = get_list_nums_from_str(numbers_list)
    xmax = str(sum(numbers_list))
    return plot_title, numbers_string, numbers_labels, numbers_loop_max, xmax


def main():
    data_filename = filedialog.askopenfilename(initialdir=Path(currfile_dir))
    if data_filename == "":
        print("Exited, by clicking Cancel")
        return
    plot_title, numbers_string, numbers_labels, numbers_loop_max, xmax = get_file_data(
        data_filename
    )
    # print(plot_title, numbers_string, numbers_labels, numbers_loop_max)

    # Create a Path object from the file path
    path_obj = Path(data_filename)

    # Get the file name from the Path object using the name attribute
    filename = path_obj.stem
    # filename = input("Enter the base filename to be added to the prefix dp_: \n")
    # if not filename:
    #     filename = "dp_1"
    # set names of files that are made
    tex_output_path = currfile_dir / f"{filename}.tex"
    pdf_path = currfile_dir / f"{filename}.pdf"
    png_path = currfile_dir / f"{filename}.png"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()

    # Replace the placeholders in the LaTeX template

    tex_template_txt = tex_template_txt.replace("<<plot_title>>", plot_title)
    tex_template_txt = tex_template_txt.replace(
        "<<numbers_loop_max>>", numbers_loop_max
    )
    tex_template_txt = tex_template_txt.replace("<<xmax>>", xmax)
    tex_template_txt = tex_template_txt.replace("<<numbers_labels>>", numbers_labels)
    tex_template_txt = tex_template_txt.replace("<<numbers_string>>", numbers_string)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the PDFs to PNGs
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
