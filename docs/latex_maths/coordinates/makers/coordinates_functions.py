"""
Module of functions to return diagram dictionary for LaTeX
"""

import random


def get_coordinates_dict(num=None):
    coord_dict = get_points_dict(num)
    coords_sections_dict = dict()
    coords_sections_dict["points_to_list"] = format_latex_coordinates_for_listing(coord_dict)
    coords_sections_dict["points_to_plot"] = format_latex_coordinates_for_plotting(coord_dict)
    return coords_sections_dict



def get_points_dict(num=None):
    # limit to max of 20
    if num is None or num > 20:
        num = random.randint(5, 20)  # Randomly choose how many points to generate
    coord_labels_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    coord_dict = {}
    used_x_values = set()  # Track used x-values
    used_y_values = set()  # Track used y-values
    for i in range(num):
        label = coord_labels_list[i]  # Get the next available letter
        x, y = random_coordinate(used_x_values, used_y_values)  # Ensure unique values
        coord_dict[label] = (x, y)
    return coord_dict


def random_coordinate(used_x_values, used_y_values):
    while True:
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        # Check constraints
        if y == -1:  # Avoid y = -1
            continue
        if y % 2 == 0 and (x == -1 or x == -2):  # Avoid x = 1 or -2 when y is even
            continue
        if y in used_y_values:  # Avoid reused y-values
            continue
        if x in used_x_values:  # Avoid reused x-values
            continue

        # If valid, mark x and y as used
        used_x_values.add(x)
        used_y_values.add(y)
        break
    return x, y


def format_latex_coordinates_for_listing(coord_dict):
    latex_str = r"\[" + "\n"
    latex_str += r"\begin{array}{lllll}" + "\n"  # Define 5 columns
    # Create list of formatted points
    items = [f"{key}({x}, {y})" for key, (x, y) in coord_dict.items()]
    # Split items into rows of 5 points
    rows = [items[i : i + 5] for i in range(0, len(items), 5)]
    # Add rows to LaTeX string with `\quad` spacing
    for row in rows:
        latex_str += " \quad & ".join(row) + r" \\" + "\n"
    latex_str += r"\end{array}" + "\n"
    latex_str += r"\]"
    return latex_str



def format_latex_coordinates_for_plotting(coord_dict):
    latex_str = ""
    for name, (x, y) in coord_dict.items():
        latex_str += f"\\fill ({x},{y}) circle (4pt);\n"
        latex_str += f"\\node[xshift=1.9em, yshift=7pt] at ({x},{y}) {{\\small {name}({x},{y})}};\n"
    return latex_str

# print(get_coordinates_dict(20)["points_to_plot"])
