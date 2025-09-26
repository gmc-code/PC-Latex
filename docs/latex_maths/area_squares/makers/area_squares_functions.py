"""
Module of functions to return diagram dictionary for LaTeX
"""
import random


def get_ints_shuffled_one_dig_first():
    # Define the range of integers
    numbers1 = list(range(1, 10))
    numbers2 = list(range(10, 21))
    # Shuffle each list
    random.shuffle(numbers1)
    random.shuffle(numbers2)
    # Join the two lists
    numbers = numbers1 + numbers2
    return numbers


def get_rotations_shuffled():
    # Define the range of angles with weighting for 0
    angles = [0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] * 2
    # Shuffle list
    random.shuffle(angles)
    return angles


def get_area_squares_dict(side_int=None, rotation=None):
    if side_int is None:
        side_int = get_ints_shuffled_one_dig_first()[0]
    if rotation is None:
        rotation = get_rotations_shuffled()[0]

    calc_sidelength = side_int
    sidelength = round(random.uniform(0, 1.5) + 1.5, 3)
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
