from pathlib import Path
import subprocess
import os
import time
import magick_pdf_to_png
import random



currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "times_tables_template.tex"
# texans_template_path = currfile_dir / "times_tables_template.tex"


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




def generate_latex(times_table,template):
    multiples = [times_table * i for i in range(1, 11)]
    missing_symbol = '\\textsubscript{. . . .}'

    template = template.replace("{TIMES_TABLE}", str(times_table))
    template = template.replace("{MULTIPLES}", ', '.join(map(str, multiples)))
    template = template.replace("{MISSING_1}", f"{multiples[0]}, {missing_symbol}, {multiples[2]}, {missing_symbol}, {multiples[4]}, {missing_symbol}, {multiples[6]}, {missing_symbol}, {multiples[8]}, {missing_symbol}")
    template = template.replace("{MISSING_2}", f"{multiples[0]}, {missing_symbol}, {missing_symbol}, {multiples[3]}, {missing_symbol}, {missing_symbol}, {multiples[6]}, {missing_symbol}, {missing_symbol}, {multiples[9]}")
    template = template.replace("{MISSING_3}", f"{multiples[0]}, {missing_symbol}, {missing_symbol}, {missing_symbol}, {missing_symbol}, {missing_symbol}, {missing_symbol}, {missing_symbol}, {missing_symbol}, {missing_symbol}")

    table_rows = ""
    for i in range(1, 11):
        table_rows += f"$ {times_table} \\times {i} = {multiples[i-1]} $ & "
        table_rows += f"$ {times_table} \\times {i} = {missing_symbol} $ & "
        table_rows += f"$ {times_table} \\times {missing_symbol} = {missing_symbol} $ & "
        table_rows += f"$ {missing_symbol} \\times {missing_symbol} = {missing_symbol} $ \\\\ \hline\n"
    template = template.replace("{TIMES_TABLE_SECTION}", table_rows)
    equations = [f"$ {times_table} \\times {i} = {missing_symbol} $" for i in range(1, 11)]
    random.shuffle(equations)
    randomized_rows = generate_randomized_section(times_table)
    template = template.replace("{RANDOMIZED_SECTION}", randomized_rows)
    return template



def generate_randomized_section(times_table):
    """
    Generates a randomized LaTeX tabular section for a specific times table (1-10).
    Each column contains the same times table but in a different randomized order.

    Args:
        times_table (int): The times table to generate (e.g., 6 for the 6 times table).

    Returns:
        str: LaTeX formatted string with randomized equations.
    """
    # Generate the times table equations
    equations = [f"${times_table} \\times {i} = \\fivedots$" for i in range(1, 11)]
    # Create 4 columns, each with a different shuffle of the same times table
    shuffled_tables = []
    for _ in range(4):
        shuffled = equations[:]  # Copy the original list
        random.shuffle(shuffled)  # Shuffle independently
        shuffled_tables.append(shuffled)
    # Build LaTeX tabular structure
    latex_table = ""  ##"\\begin{center}\n\\begin{tabular}{|" + "c|"*4 + "}\n\\hline\n"
    # Generate 10 rows where each column has a different shuffle of the times table
    for i in range(10):  # 10 rows
        row = " & ".join(shuffled_tables[col][i] for col in range(4))  # Each column has a different order
        latex_table += row + r" \\ \hline" + "\n"
    latex_table += "\\end{tabular}\n\\end{center}"
    return latex_table


def main():
    while True:
        try:
            times_table = int(input("Enter a times table (2-10): "))
            if 2 <= times_table <= 10:
                break
            else:
                print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    filename = input("Enter the base filename to be added to the prefix tt_: \n")
    if not filename:
        filename = times_table
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"tt_{filename}_q.tex"
    pdf_path = currfile_dir / f"tt_{filename}_q.pdf"
    png_path = currfile_dir / f"tt_{filename}_q.png"




    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()

    latex_code = generate_latex(times_table,tex_template_txt)

    # Write the question diagram tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(latex_code)


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
