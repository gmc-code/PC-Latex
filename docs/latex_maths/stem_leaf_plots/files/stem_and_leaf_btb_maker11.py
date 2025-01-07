from pathlib import Path
import subprocess
from tkinter import filedialog
import time
import magick_pdf_to_png
from collections import namedtuple

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "stem_and_leaf_btb_template.tex"

Maindata = namedtuple("Maindata", ["title", "keystem", "keyleaf", "keyvalue"])


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


def btbstemplotdata(
    new_num_list,
    new_num_list2,
    interval,
    multiplier,
    max_dp,
):
    d = []
    for val in sorted(data):
        val = int(val)
        stm, lf = divmod(val, interval)
        d.append((int(stm), int(lf)))
    stems, leafs = list(zip(*d))
    laststemused = min(stems) - 1
    data = ""
    for s, l in d:
        # first time with new stem
        if laststemused < s:
            laststemused += 1
            data += f"\\\\ \n{s} & {l}"
        else:
            # jsut add leaf with same stem
            data += f" {l}"
    data += f"\\\\"
    #
    stem1, leaf1 = d[0]
    key_value = int(str(stem1) + str(leaf1))
    if multiplier == 1:
        real_key_value = key_value
    else:
        real_key_value = round(key_value / multiplier, max_dp)

    main_data = Maindata(main_title, str(stem1), str(leaf1), str(real_key_value))
    return main_data, data[4:]


def get_file_data(filename):
    # open the text file and read the numbers
    with open(filename) as f:
        # read the first line and store it in a variable
        main_title = f.readline().strip()
        # read the second line and store it in a variable
        leaf1_title = f.readline().strip()
        # read the third line and store it in a variable
        numbers_string = f.readline().strip()
        # read the fourth line and store it in a variable
        leaf2_title = f.readline().strip()
        # read the fifth line and store it in a variable
        numbers_string2 = f.readline().strip()
    #
    numbers_list = get_list_from_str(numbers_string)
    numbers_list = get_list_nums_from_str(numbers_list)
    # get rid of decimals by * by power of 10
    max_dp = max(
        len(str(x).split(".")[1]) if "." in str(x) else 0 for x in numbers_list
    )
    multiplier = 10**max_dp
    new_num_list = [int(x * multiplier) for x in numbers_list]
    # ########################
    numbers_list2 = get_list_from_str(numbers_string2)
    numbers_list2 = get_list_nums_from_str(numbers_list2)
    # get rid of decimals by * by power of 10
    max_dp2 = max(
        len(str(x).split(".")[1]) if "." in str(x) else 0 for x in numbers_list2
    )
    multiplier2 = 10**max_dp2
    new_num_list2 = [int(x * multiplier2) for x in numbers_list2]
    # ########################
    # get interval based on no of digits for first data group
    interval_multiplier = max(len(str(x)) for x in new_num_list) - 1
    interval = 10**interval_multiplier
    # only want 1 in the leaf
    if interval > 10:
        interval = 10
        key_data, data = btbstemplotdata(
            new_num_list,
            new_num_list2,
            interval,
            multiplier,
            max_dp,
        )
    return main_title, key_data, leaf1_title, leaf2_title, data


def main():
    data_filename = filedialog.askopenfilename(initialdir=Path(currfile_dir))
    if data_filename == "":
        print("Exited, by clicking Cancel")
        return
    main_title, key_data, leaf1_title, leaf2_title, data = get_file_data(data_filename)

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

    tex_template_txt = tex_template_txt.replace("<<title>>", main_title)
    tex_template_txt = tex_template_txt.replace("<<keystem>>", key_data.keystem)
    tex_template_txt = tex_template_txt.replace("<<keyleaf>>", key_data.keyleaf)
    tex_template_txt = tex_template_txt.replace("<<keyvalue>>", key_data.keyvalue)
    tex_template_txt = tex_template_txt.replace("<<leaf1_title>>", leaf1_title)
    tex_template_txt = tex_template_txt.replace("<<leaf2_title>>", leaf2_title)
    tex_template_txt = tex_template_txt.replace("<<data>>", data)

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
