"""
Module of functions to return diagram dictionary for LaTeX
"""

import random
import math


def get_side_pairs():
    pairs = [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 5),
             (4, 6), (4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (6, 7), (6, 8), (6, 9), (7, 8), (7, 9), (8, 9)]
    random.shuffle(pairs)
    return pairs


def get_heights():
    values = [1, 1]  + [2, 3, 4] * 5 +  [6, 7, 8]
    random.shuffle(values)
    return values


def get_rotations_shuffled():
    # Define the range of angles with weighting for 0
    # angles = [0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] * 2
     # angles = [0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] + [90, 90, 90, 90, 90, 100, 110, 120, 80, 70, 60] + [180, 180, 180, 180, 180, 190, 200, 210, 170, 160, 150] + [270, 270, 270, 270, 270, 280, 290, 300, 260, 250, 240]
    angles = [0, 0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] * 3 + [40, 40] + [-40, -40]
    # angles = [0] * 20
    # Shuffle list
    random.shuffle(angles)
    return angles


def skew_factor_x():
    return random.uniform(0.3, 1.0)


def get_volume_rectangular_prisms_dict(side_pair=None, height=None, rotation=None):
    # 1 longer than 2 and to scale
    if side_pair is None:
        side_pair = get_side_pairs()[0]

    if rotation is None:
        rotation = 0 # get_rotations_shuffled()[0]

    calc_l = side_pair[1]  #longer
    calc_w = side_pair[0]  # shorter
    calc_H = height
    calc_V = calc_l * calc_w * calc_H

    w = round(random.uniform(0, 1.0) + 1.5, 3)
    l = round(w * (calc_l / calc_w), 3)
    H = round(l * (calc_H / calc_l), 3)

    if (l + 0.7*w) > 4.0:
        ratio = 4.0 / (l + 0.7*w)
        l = round(l * ratio, 3)
        w = round(w * ratio, 3)
        H = round(H * ratio, 3)




    # % skew shift
    fx = skew_factor_x()
    # fy = skew_factor_y()
    fy = math.sqrt(1 - (fx)**2)
    dx = round(0.7 * fx * w,3)
    dy = round(0.7 * fy * w,3)

    # gap_to_fill = "\\dotuline{~~~~~~~}"

    vertices_lists = [["A", "B", "C", "D", "E", "F", "G", "H"],
                      ["E", "F", "G", "H", "K", "L", "M", "N"],
                      ["K", "L", "M", "N", "Q", "R", "S", "T"],
                      ["Q", "R", "S", "T", "W", "X", "Y", "Z"]]
    vertices_labels = random.choice(vertices_lists)

    # random.shuffle(vertices_labels)
    # vertexA
    vA = vertices_labels[0]
    vB = vertices_labels[1]
    vC = vertices_labels[2]
    vD = vertices_labels[3]
    vE = vertices_labels[4]
    vF = vertices_labels[5]
    vG = vertices_labels[6]
    vH = vertices_labels[7]

    kv = dict()

    kv["calc_l"] = f"{calc_l}"
    kv["calc_w"] = f"{calc_w}"
    kv["calc_H"] = f"{calc_H}"
    kv["calc_V"] = f"{calc_V}"
    kv["length"] = f"{l}"
    kv["width"] = f"{w}"
    kv["height"] = f"{H}"
    kv["rotation"] = f"{rotation}"
    kv["dx"] = f"{dx}"
    kv["dy"] = f"{dy}"

    kv["vA"] = f"{vA}"
    kv["vB"] = f"{vB}"
    kv["vC"] = f"{vC}"
    kv["vD"] = f"{vD}"
    kv["vE"] = f"{vE}"
    kv["vF"] = f"{vF}"
    kv["vG"] = f"{vG}"
    kv["vH"] = f"{vH}"

    kv["calc_l_value"] = f"{calc_l}"
    kv["calc_w_value"] = f"{calc_w}"
    kv["calc_H_value"] = f"{calc_H}"
    kv["calc_V_value"] = f"{calc_V}"

    return kv

# print(get_volume_rectangular_prisms_dict().items())