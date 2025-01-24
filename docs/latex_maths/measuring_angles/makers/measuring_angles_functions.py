"""
Module of functions to return diagram dictionary for LaTeX
"""

import random


def get_angles_for_measuring_dict(ang_type):
    if ang_type == 4:
        ang_type = random.randint(1, 3)
    if ang_type not in [1,2,3]:
        ang_type = random.randint(1, 3)
    match ang_type:
        case 1:
            angleB = int(random.randint(10, 85))
        case 2:
            angleB = int(random.randint(95, 175))
        case 3:
            angleB = int(random.randint(185, 350))


    if random.random() < 0.50:  # 50% chance
        rotationAngleValue = 0
    else:
        rotationAngleValue = random.randint(0, 60)


    arm_length = 4  #+ random.uniform(0, 2)
    ABlength = arm_length
    BClength = arm_length

    vertices_lists = [["A", "B", "C"], ["F", "G", "H"], ["L", "M", "N"],
                      ["R", "S", "T"], ["X", "Y", "Z"]]
    vertices_labels = random.choice(vertices_lists)
    gaps = r"\dotuline{~~~~~~~}"

    random.shuffle(vertices_labels)
    angleALabel = vertices_labels[0]
    angleBLabel = vertices_labels[1]
    angleCLabel = vertices_labels[2]

    kv = dict()
    kv["rotationAngleValue"] = f"{rotationAngleValue}"
    kv["angleBValue"] = f"{angleB}"
    kv["ABlengthValue"] = f"{ABlength}"
    kv["BClengthValue"] = f"{BClength}"

    kv["angleALabel"] = angleALabel
    kv["angleBLabel"] = angleBLabel
    kv["angleCLabel"] = angleCLabel

    kv["angleBDisplayValue"] = fr"$\theta^\circ = {angleB}^\circ$"

    kv["angleBDisplayValue_q"] = fr"$\theta^\circ = {gaps}^\circ$"

    return kv
