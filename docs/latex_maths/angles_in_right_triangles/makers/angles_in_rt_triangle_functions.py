"""
Module of functions to return diagram dictionary for LaTeX
Make C = 90; B = 90 - A; find A
"""
import random


def get_angles_in_rt_triangle_dict():
    angleAValue = int(random.randint(0,40)+25)
    angleBValue = 90 - angleAValue
    angleCValue = 90
    sideCValue = random.uniform(0, 1) + 3
    rotationAngleValue = int(random.randint(0,360))
    # gap_to_fill = "\\dotuline{~~~~~~~}"

    vertices_lists = [["A", "B", "C"], ["F", "G", "H"], ["L", "M", "N"], ["R", "S", "T"], ["X", "Y", "Z"]]
     vertices_labels = random.choice(vertices_lists)

    random.shuffle( vertices_labels)
    angleALabel =  vertices_labels[0]
    angleBLabel =  vertices_labels[1]
    angleCLabel =  vertices_labels[2]

    kv = dict()
    kv["angleAValue"] = f"{angleAValue}"
    kv["angleBValue"] = f"{angleBValue}"
    kv["angleCValue"] = f"{angleCValue}"
    kv["sideCValue"] = f"{sideCValue}"
    kv["rotationAngleValue"] = f"{rotationAngleValue}"

    kv["angleALabel"] = f"{angleALabel}"
    kv["angleBLabel"] = f"{angleBLabel}"
    kv["angleCLabel"] = f"{angleCLabel}"

    kv["angleAValueDisplay"] = f"{angleAValue}"
    kv["angleBValueDisplay"] = f"{angleBValue}"

    unknownpos = random.randint(1,2)
    match unknownpos:
        case 1:
            kv["angleAValueDisplay"] = f"\\theta"
            # kv["angleLabel1"] = f"{angleALabel}"
            kv["angleLabel2"] = f"{angleBLabel}"
            kv["angleValue1"] = f"{angleAValue}"
            kv["angleValue2"] = f"{angleBValue}"
        case 2:
            kv["angleBValueDisplay"] = f"\\theta"
            # kv["angleLabel1"] = f"{angleBLabel}"
            kv["angleLabel2"] = f"{angleALabel}"
            kv["angleValue1"] = f"{angleBValue}"
            kv["angleValue2"] = f"{angleAValue}"
    return kv