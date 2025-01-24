"""
Module of functions to return diagram dictionary for LaTeX
"""
def get_lined_page_diagram(num=0):
    if num is None or num == 0:
        num = 26
    steps = 28
    draw_line = r"\draw[black,line width=0.5pt] (current page.north west) ++(2cm,-2cm-{y} pt) -- ++(\paperwidth-4cm,0);"
    diagram_text = ""
    for i in range(1, num + 1):
        y = i * steps
        new_draw_line = draw_line.format(y=y)
        diagram_text += new_draw_line + "\n"
    return diagram_text


def get_lined_paper_diagram(num=0):
    if num is None or num == 0:
        num = 26
    steps = 28
    draw_line = r"\draw[black,line width=0.5pt] (current page.north west) ++(0cm,-0cm-{y} pt) -- ++(\paperwidth-0cm,0);"
    diagram_text = ""
    for i in range(1, num + 1):
        y = i * steps
        new_draw_line = draw_line.format(y=y)
        diagram_text += new_draw_line + "\n"
    return diagram_text




def get_lined_paper_height(num=4):
    if num is None or num < 1:
        num = 4
    steps = 28
    extra_height = 14
    paper_height = num * steps + extra_height
    return str(paper_height)
