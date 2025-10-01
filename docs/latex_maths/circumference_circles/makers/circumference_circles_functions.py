"""
Module of functions to return diagram dictionary for LaTeX
"""
import random
import math


def random_float_1dp():
    return round(random.uniform(0.1, 10.0), 1)

def get_random_float_1dp_list():
    result = set()
    while len(result) < 20:
        result.add(random_float_1dp())
    return list(result)


def get_rotations_shuffled():
    # Define the range of angles with weighting for 0
    # angles = [0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] + [90, 90, 90, 90, 90, 100, 110, 120, 80, 70, 60] + [180, 180, 180, 180, 180, 190, 200, 210, 170, 160, 150] + [270, 270, 270, 270, 270, 280, 290, 300, 260, 250, 240]
    angles = [0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, -10, -20, -30] + [45, 90, 90, 80, 100] + [135, 180, 180, 170, 190] + [225, 270, 270, 315]
    # angles = [0] * 20
    # Shuffle list
    random.shuffle(angles)
    return angles


def get_circumference_circles_dict(radius=None, rotation=None):
    if radius is None:
        radius = random_float_1dp()
    if rotation is None:
        rotation = get_rotations_shuffled()[0]

    draw_radius = round(random.uniform(0, 1.0) + 1.3, 3)
    calc_radius_value = radius
    calc_circumference_value = round(2 * math.pi * radius,3)

    # gap_to_fill = "\\dotuline{~~~~~~~}"

    kv = dict()

    kv["calc_radius"] = f"{radius}"
    kv["draw_radius"] = f"{draw_radius}"
    kv["rotation"] = f"{rotation}"

    kv["calc_radius_value"] = f"{calc_radius_value}"
    kv["calc_circumference_value"] = f"{calc_circumference_value}"

    return kv
