import numpy as np
from pathlib import Path
import subprocess
from tkinter import filedialog
import time
import magick_pdf_to_png

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "dot_plot_template.tex"


def convert_to_pdf(tex_path, currfile_dir, aux_path):
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


def get_np_array(filename):
    # open the text file and read the numbers
    with open(filename) as f:
        # read the first line and store it in a variable
        plot_xlabel = f.readline().strip()
        # read the second line and store it in a variable
        numbers_string = f.readline().strip()
        if ", " in numbers_string:
            numbers = numbers_string.split(", ")
        elif "," in numbers_string:
            numbers = numbers_string.split(",")
        else:
            numbers = numbers_string.split(" ")

    # convert the numbers strings to integers
    if "." in numbers_string:
        numbers = [float(n) for n in numbers]
    else:
        numbers = [int(n) for n in numbers]
    # create a numpy array from the numbers
    return plot_xlabel, np.array(numbers)


def dotplot(input_x):
    # get 2 arrays in order with counts for each value
    unique_values, counts = np.unique(input_x, return_counts=True)
    # get max counts for pdf height
    max_counts = np.max(counts)
    # # Convert into coordinates space delimited for latex
    coords = ""
    for idx, value in enumerate(unique_values):
        for counter in range(1, counts[idx] + 1):
            coord = (value, counter)
            coords += str(coord)
    return coords, max_counts


def main():
    data_filename = filedialog.askopenfilename(initialdir=Path(currfile_dir))
    if data_filename == "":
        print("Exited, by clicking Cancel")
        return
    plot_xlabel, num_array = get_np_array(data_filename)
    latex_coords, max_counts = dotplot(num_array)
    pdf_height = str(min(8, 1.4 + max_counts / 4))
    # print(pdf_height)
    # Get the maximum value
    max_val = str(np.max(num_array) + 0.5)
    # Get the minimum value
    min_val = str(np.min(num_array) - 0.5)

    # Create a Path object from the file path
    path_obj = Path(data_filename)

    # Get the file name from the Path object using the name attribute
    filename = path_obj.stem
    # filename = input("Enter the base filename to be added to the prefix dp_: \n")
    # if not filename:
    #     filename = "dp_1st"
    # set names of files that are made
    tex_output_path = currfile_dir / f"{filename}.tex"
    pdf_path = currfile_dir / f"{filename}.pdf"
    png_path = currfile_dir / f"{filename}.png"
    aux_path = currfile_dir / "temp"
    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()

    # Replace the placeholders in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<coords>>", latex_coords)
    tex_template_txt = tex_template_txt.replace("<<xlabel>>", plot_xlabel)
    tex_template_txt = tex_template_txt.replace("<<max_val>>", max_val)
    tex_template_txt = tex_template_txt.replace("<<min_val>>", min_val)
    tex_template_txt = tex_template_txt.replace("<<height>>", pdf_height)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the PDFs to PNGs
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
