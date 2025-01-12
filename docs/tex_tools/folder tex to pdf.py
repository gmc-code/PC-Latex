from pathlib import Path
import subprocess
import os
from tkinter import filedialog


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




def main():
    currfile_dir = Path(__file__).parent
    tex_dir = filedialog.askdirectory(initialdir=currfile_dir)
    if tex_dir == "":
        print("Exited, by clicking Cancel")
        return

    for tex_path in Path(tex_dir).glob('*.tex'):
        convert_to_pdf(tex_path, tex_dir)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
