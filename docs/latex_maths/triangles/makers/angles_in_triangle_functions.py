"""
Module of functions to return diagram dictionary for LaTeX
"""
import random


def get_angles_in_triangle_dict():
    angleAValue = int(random.randint(0,40)+25)
    angleBValue = int(random.randint(0,40)+25)
    angleCValue = int(180-angleAValue-angleBValue)
    angleBCValue = int(angleBValue+angleCValue)
    sideCValue = random.uniform(0, 1) + 3
    rotationAngleValue = int(random.randint(0,20))
    # gap_to_fill = "\dotuline{~~~~~~~}"

    kv = dict()
    kv["angleAValue"] = f"{angleAValue}"
    kv["angleBValue"] = f"{angleBValue}"
    kv["angleCValue"] = f"{angleCValue}"
    kv["angleBCValue"] = f"{angleBCValue}"
    kv["sideCValue"] = f"{sideCValue}"
    kv["rotationAngleValue"] = f"{rotationAngleValue}"

    kv["angleCalcAValue"] = f"{angleAValue}"
    kv["angleCalcBValue"] = f"{angleBValue}"
    kv["angleCalcCValue"] = f"{angleCValue}"
    kv["angleCalcBCValue"] = f"{angleBCValue}"

    return kv