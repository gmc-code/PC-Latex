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
    # angles = [0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] + [90, 90, 90, 90, 90, 100, 110, 120, 80, 70, 60] + [180, 180, 180, 180, 180, 190, 200, 210, 170, 160, 150] + [270, 270, 270, 270, 270, 280, 290, 300, 260, 250, 240]
    angles = [0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] + [90, 90, 90, 80, 100] + [180, 180, 180, 170, 190] + [270, 270, 270, 270]
    # angles = [0] * 20
    # Shuffle list
    random.shuffle(angles)
    return angles


def get_area_triangles_acute_dict(side_pair=None, rotation=None):
    # 1 longer than 2 and to scale
    if side_pair is None:
        side_pair = get_side_pairs()[0]
    if rotation is None:
        rotation = get_rotations_shuffled()[0]

    calc_base = side_pair[1] # longer
    calc_height = side_pair[0] # shorter
    height = round(random.uniform(0, 1.0) + 1.5, 3)
    base = round(height * (calc_base / calc_height), 3)

    if base > 8:
        ratio = 8 / base
        base = round(base * ratio, 3)
        height = round(height * ratio, 3)

    leftoffset = round(random.uniform(0, base - 1) + 0.5, 3)
    calcarea_value = 0.5 * calc_base * calc_height

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

    kv["calc_base"] = f"{calc_base}"
    kv["calc_height"] = f"{calc_height}"
    kv["base"] = f"{base}"
    kv["height"] = f"{height}"
    kv["leftoffset"] = f"{leftoffset}"
    kv["rotation"] = f"{rotation}"

    kv["vA"] = f"{vA}"
    kv["vB"] = f"{vB}"
    kv["vC"] = f"{vC}"
    kv["vD"] = f"{vD}"

    kv["calc_base_value"] = f"{calc_base}"
    kv["calc_height_value"] = f"{calc_height}"
    kv["calcarea_value"] = f"{calcarea_value}"

    return kv
