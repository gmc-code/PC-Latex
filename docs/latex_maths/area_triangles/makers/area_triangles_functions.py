"""
Module of functions to return diagram dictionary for LaTeX
"""

import random


def get_side_pairs():
    pairs = [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 5),
             (4, 6), (4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (6, 7), (6, 8), (6, 9), (7, 8), (7, 9), (8, 9)]
    random.shuffle(pairs)
    return pairs


def get_rotations_shuffled():
    # Define the range of angles with weighting for 0
    angles = [0, 0, 0, 0, 0, 10, 30, -10, -30, -45] * 2
    # Shuffle list
    random.shuffle(angles)
    return angles



def get_area_rectangles_dict(side_pair=None, rotation=None):
    # 1 longer than 2 and to scale
    if side_pair is None:
        side_pair = get_side_pairs()[0]
    if rotation is None:
        rotation = get_rotations_shuffled()[0]

    calc_sidelength1 = side_pair[1]
    calc_sidelength2 = side_pair[0]
    sidelength1 = round(random.uniform(0, 1.5) + 2, 3)
    sidelength2 = round(sidelength1 * (calc_sidelength2 / calc_sidelength1), 3)
    calcarea_value = calc_sidelength1 * calc_sidelength2

    # gap_to_fill = "\\dotuline{~~~~~~~}"

    vertices_lists = [["A", "B", "C", "D"], ["E", "F", "G", "H"],
                      ["K", "L", "M", "N"], ["Q", "R", "S", "T"],
                      ["W", "X", "Y", "Z"]]
    vertices_labels = random.choice(vertices_lists)

    # random.shuffle(vertices_labels)
    # vertexA
    vA = vertices_labels[0]
    vB = vertices_labels[1]
    vC = vertices_labels[2]
    vD = vertices_labels[3]

    kv = dict()

    kv["calc_sidelength1"] = f"{calc_sidelength1}"
    kv["calc_sidelength2"] = f"{calc_sidelength2}"
    kv["sidelength1"] = f"{sidelength1}"
    kv["sidelength2"] = f"{sidelength2}"
    kv["rotation"] = f"{rotation}"

    kv["vA"] = f"{vA}"
    kv["vB"] = f"{vB}"
    kv["vC"] = f"{vC}"
    kv["vD"] = f"{vD}"

    kv["calcside_value1"] = f"{calc_sidelength1}"
    kv["calcside_value2"] = f"{calc_sidelength2}"
    kv["calcarea_value"] = f"{calcarea_value}"

    return kv
