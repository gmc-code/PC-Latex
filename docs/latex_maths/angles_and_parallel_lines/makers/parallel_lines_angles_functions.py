"""
Module of functions to return diagram dictionary for LaTeX
"""

import random
import math


def cos_deg(degrees):
    return math.cos(math.radians(degrees))


def sin_deg(degrees):
    return math.sin(math.radians(degrees))


def corresponding_random():
    angle_pairs = [("a", "e"), ("b", "f"), ("c", "g"), ("d", "h")]
    my_tuple = random.choice(angle_pairs)
    if random.randint(0, 1) == 1:
        my_tuple = tuple(x for x in reversed(my_tuple))
    return my_tuple


def alternate_random():
    angle_pairs = [("a", "g"), ("d", "f")]
    my_tuple = random.choice(angle_pairs)
    if random.randint(0, 1) == 1:
        my_tuple = tuple(x for x in reversed(my_tuple))
    return my_tuple


def cointerior_random():
    angle_pairs = [("a", "f"), ("d", "g")]
    my_tuple = random.choice(angle_pairs)
    if random.randint(0, 1) == 1:
        my_tuple = tuple(x for x in reversed(my_tuple))
    return my_tuple


def vertically_opposite_random():
    angle_pairs = [("a", "c"), ("b", "d"), ("e", "g"), ("f", "h")]
    my_tuple = random.choice(angle_pairs)
    if random.randint(0, 1) == 1:
        my_tuple = tuple(x for x in reversed(my_tuple))
    return my_tuple


def consecutive_exterior_random():
    angle_pairs = [("b", "e"), ("c", "h")]
    my_tuple = random.choice(angle_pairs)
    if random.randint(0, 1) == 1:
        my_tuple = tuple(x for x in reversed(my_tuple))
    return my_tuple


def alternate_exterior_random():
    angle_pairs = [("b", "h"), ("c", "e")]
    my_tuple = random.choice(angle_pairs)
    if random.randint(0, 1) == 1:
        my_tuple = tuple(x for x in reversed(my_tuple))
    return my_tuple


def make_angles_latex(angles_to_label, angles_to_value, angle_dict):
    anglestext = ""
    for ang in angles_to_label:
        latex_str = angle_latex_strings(ang, ang)
        anglestext += latex_str + "\n"
    for ang in angles_to_value:
        ang_text = str(angle_dict[ang]) + "^\circ"
        latex_str = angle_latex_strings(ang, ang_text)
        anglestext += latex_str + "\n"
    return anglestext


def angle_latex_strings(angle_letter, angle_text):
    match angle_letter:
        # %% Point A a-d; Point B e-h
        case "a":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=te--A--p1e}};'
        case "b":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=p1e--A--ts}};'
        case "c":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=ts--A--p1s}};'
        case "d":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=p1s--A--te}};'
        case "e":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=te--B--p2e}};'
        case "f":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=p2e--B--ts}};'
        case "g":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=ts--B--p2s}};'
        case "h":
            text = f'\draw pic["${angle_text}$", draw=black, -, angle eccentricity=1.8, angle radius=0.4cm] {{angle=p2s--B--te}};'
    return text


def get_parallel_lines_angles_dict(angles_to_label, angles_to_value):

    angleA = int(random.randint(30, 150))
    angleB = 180 - angleA
    linelength = 4
    paralleldistance = 1.5
    transangle = 0
    transprojectinglength = 1.5
    rotationAngle = int(random.randint(0, 360))

    # % Calculate the translength
    translength = 2 * transprojectinglength + paralleldistance / cos_deg((90 - angleA) + transangle)

    # % Calculate the x and y components of the first parallel line starting at 0, 0
    parIstartx = 0
    parIstarty = 0
    parIendx = linelength * cos_deg(angleA)
    parIendy = linelength * sin_deg(angleA)

    # % Calculate the x and y offsets for the second line; use x shift only
    xoffset = paralleldistance / sin_deg(angleA)
    yoffset = 0

    # % Calculate the x and y components of the second parallel line starting at parIstartx, parIstarty
    parIIstartx = parIstartx + xoffset
    parIIstarty = parIstarty + yoffset
    parIIendx = parIendx + xoffset
    parIIendy = parIendy + yoffset

    # % Calculate the x and y components of the transversal vector
    transparIendx = 0.5 * translength * cos_deg(transangle)
    transparIendy = 0.5 * translength * sin_deg(transangle)

    # % Calculate the midpoint of the parallel lines
    midpointx = 0.5 * parIendx + 0.5 * xoffset
    midpointy = 0.5 * parIendy

    # % Calculate the start and end points of the transversal
    transstartx = midpointx - 1 * transparIendx
    transstarty = midpointy - 1 * transparIendy
    transendx = midpointx + transparIendx
    transendy = midpointy + transparIendy

    kv = dict()
    kv["rotationAngle"] = f"{rotationAngle}"
    kv["parIstartx"] = f"{parIstartx}"
    kv["parIstarty"] = f"{parIstarty}"
    kv["parIendx"] = f"{parIendx}"
    kv["parIendy"] = f"{parIendy}"

    kv["parIIstartx"] = f"{parIIstartx}"
    kv["parIIstarty"] = f"{parIIstarty}"
    kv["parIIendx"] = f"{parIIendx}"
    kv["parIIendy"] = f"{parIIendy}"

    kv["transstartx"] = f"{transstartx}"
    kv["transstarty"] = f"{transstarty}"
    kv["transendx"] = f"{transendx}"
    kv["transendy"] = f"{transendy}"

    variables = ["alabel", "blabel", "clabel", "dlabel", "elabel", "flabel", "glabel", "hlabel"]
    values = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for var, val in zip(variables, values):
        kv[var] = f"{val}"

    variables = ["aval", "bval", "cval", "dval", "eval", "fval", "gval", "hval"]
    values = [angleA, angleB, angleA, angleB, angleA, angleB, angleA, angleB]
    for var, val in zip(variables, values):
        kv[var] = f"{val}"

    angle_dict = dict()
    variables = ["a", "b", "c", "d", "e", "f", "g", "h"]
    values = [angleA, angleB, angleA, angleB, angleA, angleB, angleA, angleB]
    for var, val in zip(variables, values):
        angle_dict[var] = f"{val}"

    kv["anglestext"] = make_angles_latex(angles_to_label, angles_to_value, angle_dict)
    kv["angle_to_find"] = f"{angles_to_label}"
    kv["angle_to_find_value"] = f"{angle_dict[angles_to_label]}"

    return kv

def get_corresponding_dict():
    anglepair = corresponding_random()
    angles_to_label = anglepair[1]
    angles_to_value = anglepair[0]
    return get_parallel_lines_angles_dict(angles_to_label, angles_to_value)


def get_alternate_dict():
    anglepair = alternate_random()
    angles_to_label = anglepair[1]
    angles_to_value = anglepair[0]
    return get_parallel_lines_angles_dict(angles_to_label, angles_to_value)


def get_cointerior_dict():
    anglepair = cointerior_random()
    angles_to_label = anglepair[1]
    angles_to_value = anglepair[0]
    return get_parallel_lines_angles_dict(angles_to_label, angles_to_value)



def get_vertically_opposite_dict():
    anglepair = vertically_opposite_random()
    angles_to_label = anglepair[1]
    angles_to_value = anglepair[0]
    return get_parallel_lines_angles_dict(angles_to_label, angles_to_value)


def get_consecutive_exterior_dict():
    anglepair = consecutive_exterior_random()
    angles_to_label = anglepair[1]
    angles_to_value = anglepair[0]
    return get_parallel_lines_angles_dict(angles_to_label, angles_to_value)


def get_alternate_exterior_dict():
    anglepair = alternate_exterior_random()
    angles_to_label = anglepair[1]
    angles_to_value = anglepair[0]
    return get_parallel_lines_angles_dict(angles_to_label, angles_to_value)


def choose_parallel_lines_angles_dict(num):
    if num is None or num == 7:
        num = random.randint(1, 6)
    match num:
        case 1:
            return get_corresponding_dict()
        case 2:
            return get_alternate_dict()
        case 3:
            return get_cointerior_dict()
        case 4:
            return get_vertically_opposite_dict()
        case 5:
            return get_consecutive_exterior_dict()
        case 6:
            return get_alternate_exterior_dict()
