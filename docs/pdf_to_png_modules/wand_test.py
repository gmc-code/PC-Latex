from wand.image import Image

# Use a raw string for Windows path to avoid escape character issues
pathtopdf = r'C:\Users\gmccarthy\Documents\PC_RTD_GITHUB_resources\PC_latex\docs\latex_maths\grids\files\grids_isometric_horizontal.pdf'

with Image(filename=pathtopdf, resolution=300) as img:
    img.format = 'png'
    img.save(filename='output.png')
