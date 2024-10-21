from pathlib import Path
import subprocess
from tkinter import filedialog


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


def main():
    currfile_dir = Path(__file__).parent
    aux_path = currfile_dir / "temp"
    tex_dir = filedialog.askdirectory(initialdir=currfile_dir)
    if tex_dir == "":
        print("Exited, by clicking Cancel")
        return

    for tex_path in Path(tex_dir).glob('*.tex'):
        convert_to_pdf(tex_path, tex_dir, aux_path)

if __name__ == "__main__":
    print("starting")
    main()
    print("finished")