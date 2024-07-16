"""
Module of functions to return diagram dictionary for LaTeX
Make C = 90; B = 90 - A; find A
"""
import random


def get_angles_in_rt_triangle_dict():
    angleAValue = int(random.randint(0,40)+25)
    angleBValue = 90 - angleAValue
    angleCValue = 90
    angleBCValue = int(angleBValue+angleCValue)
    sideCValue = random.uniform(0, 1) + 3
    rotationAngleValue = int(random.randint(0,360))
    # gap_to_fill = "\dotuline{~~~~~~~}"

    my_lists = [["A", "B", "C"], ["F", "G", "H"], ["L", "M", "N"], ["R", "S", "T"], ["X", "Y", "Z"]]
    my_labels = random.choice(my_lists) 

    random.shuffle(my_labels) 
    angleALabel = my_labels[0]
    angleBLabel = my_labels[1]
    angleCLabel = my_labels[2]

    kv = dict()
    kv["angleAValue"] = f"{angleAValue}"
    kv["angleBValue"] = f"{angleBValue}"
    kv["angleCValue"] = f"{angleCValue}"
    kv["angleBCValue"] = f"{angleBCValue}"
    kv["sideCValue"] = f"{sideCValue}"
    kv["rotationAngleValue"] = f"{rotationAngleValue}"

    kv["angleALabel"] = f"{angleALabel}"
    kv["angleBLabel"] = f"{angleBLabel}"
    kv["angleCLabel"] = f"{angleCLabel}"

    kv["angleCalcAValue"] = f"{angleAValue}"
    kv["angleCalcBValue"] = f"{angleBValue}"
    kv["angleCalcCValue"] = f"{angleCValue}"
    kv["angleCalcBCValue"] = f"{angleBCValue}"

    return kv