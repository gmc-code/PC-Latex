import subprocess
import os

# Path to the folder containing .tex files
folder_path = r"C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC_latex\docs\latex_science\ray_tracing\files"

# Change to the target directory
os.chdir(folder_path)

# Loop through all .tex files
for filename in os.listdir(folder_path):
    if filename.endswith(".tex"):
        print(f"Compiling {filename}...")
        subprocess.run(["pdflatex", filename])
