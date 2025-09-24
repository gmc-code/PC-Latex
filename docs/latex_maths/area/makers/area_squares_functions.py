"""
Module of functions to return diagram dictionary for LaTeX
"""
import random


def get_area_squares_dict():
    calc_sidelength = random.choice(range(2, 10, 1))
    sidelength = random.uniform(0, 1.5) + 1.5
    rotation = random.choice(range(-40, 65, 20))
    calcarea_value = calc_sidelength * calc_sidelength

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

    kv["calc_sidelength"] = f"{calc_sidelength}"
    kv["sidelength"] = f"{sidelength}"
    kv["rotation"] = f"{rotation}"

    kv["vA"] = f"{vA}"
    kv["vB"] = f"{vB}"
    kv["vC"] = f"{vC}"
    kv["vD"] = f"{vD}"

    kv["calcside_value"] = f"{calc_sidelength}"
    kv["calcarea_value"] = f"{calcarea_value}"

    return kv
