from pathlib import Path
import subprocess
from tkinter import filedialog
import time
import magick_pdf_to_png
from collections import namedtuple


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "stem_and_leaf_btb_template.tex"

# named tuple for main data to be passed easily from one function to the next and used vai dot notation insetad of using a dictionary with keys.
Keydata = namedtuple("Keydata", ["keystem", "keyleaf", "keyvalue"])


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


def make_stem_leaf_dict(num_list, interval):
    stem_leaves_dict = dict()
    for val in num_list:
        stem, leaf = divmod(val, interval)
        if stem not in stem_leaves_dict:
            stem_leaves_dict[stem] = str(leaf)
        else:
            stem_leaves_dict[stem] += " " + str(leaf)
    return stem_leaves_dict


def combine_stems(dict1, dict2):
    stems1 = list(dict1.keys())
    stems2 = list(dict2.keys())
    full_stem_list = sorted(list(set(stems1 + stems2)))
    data = ""
    for stem in full_stem_list:
        data += f"{dict1.get(stem, '')[::-1]} & {str(stem)} & {dict2.get(stem, '')} \\\\"
    return data


def get_key_data(num_list, interval, multiplier, max_dp):
    val1 = num_list[0]
    stem1, leaf1 = divmod(val1, interval)
    key_value = int(str(stem1) + str(leaf1))
    if multiplier == 1:
        real_key_value = key_value
    else:
        real_key_value = round(key_value / multiplier, max_dp)
    key_data = Keydata(str(stem1), str(leaf1), str(real_key_value))
    return key_data


def stemplotdata_btb(num_list, num2_list, interval, multiplier, max_dp):
    num_list = sorted(num_list)
    num2_list = sorted(num2_list)
    # get data
    data1 = make_stem_leaf_dict(num_list, interval)
    data2 = make_stem_leaf_dict(num2_list, interval)
    data = combine_stems(data1, data2)
    # get key_data for top of key
    key_data = get_key_data(num_list, interval, multiplier, max_dp)
    return key_data, data


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
        numbers2_string = f.readline().strip()

    #
    numbers2_list = get_list_from_str(numbers2_string)
    numbers2_list = get_list_nums_from_str(numbers2_list)
    #
    numbers_list = get_list_from_str(numbers_string)
    numbers_list = get_list_nums_from_str(numbers_list)
    # get rid of decimals by * by power of 10
    # combine lists for factors
    both_numbers_list = numbers_list + numbers2_list
    max_dp = max(
        len(str(x).split(".")[1]) if "." in str(x) else 0 for x in both_numbers_list
    )
    multiplier = 10**max_dp
    new_num_list = [int(x * multiplier) for x in numbers_list]
    new_num2_list = [int(x * multiplier) for x in numbers2_list]
    # get interval based on no of digits
    both_new_num_list = new_num_list + new_num2_list
    interval_multiplier = max(len(str(x)) for x in both_new_num_list) - 1
    interval = 10**interval_multiplier
    # only want 1 in the leaf
    if interval > 10:
        interval = 10
    key_data, data = stemplotdata_btb(
        new_num_list, new_num2_list, interval, multiplier, max_dp
    )
    return main_title, key_data, leaf1_title, leaf2_title, data


def main():
    data_filename = filedialog.askopenfilename(initialdir=Path(currfile_dir))
    if data_filename == "":
        print("Exited, by clicking Cancel")
        return
    main_title, key_data, leaf1_title, leaf2_title, data = get_file_data(data_filename)
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
    aux_path = currfile_dir / "temp"
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
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the PDFs to PNGs
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
