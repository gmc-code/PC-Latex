"""
Module of functions to return diagram dictionary for LaTeX
"""
import random


def get_ext_angle_to_triangle_dict():
    angleAValue = int(random.randint(0,40)+25)
    angleBValue = int(random.randint(0,40)+25)
    angleCValue = int(180-angleAValue-angleBValue)
    angleExtBValue = int(180-angleBValue)

    # angleBCValue = int(angleBValue+angleCValue)
    sideCValue = random.uniform(0, 1) + 3
    sideDValue = sideCValue + 1

    rotationAngleValue = int(random.randint(0,360))
    # gap_to_fill = "\dotuline{~~~~~~~}"

    my_lists = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["J", "K", "L", "M"], ["Q", "R", "S", "T"], ["X", "Y", "Z", "W"]]
    my_labels = random.choice(my_lists) 

    random.shuffle(my_labels) 
    angleALabel = my_labels[0]
    angleBLabel = my_labels[1]
    angleCLabel = my_labels[2]
    angleDLabel = my_labels[3]
    angleExtLabel = angleDLabel + angleBLabel + angleCLabel

    kv = dict()
    kv["angleAValue"] = f"{angleAValue}"
    kv["angleBValue"] = f"{angleBValue}"
    kv["angleCValue"] = f"{angleCValue}"
    kv["angleExtBValue"] = f"{angleExtBValue}"
    
    kv["sideCValue"] = f"{sideCValue}"    
    kv["sideDValue"] = f"{sideDValue}"
    kv["rotationAngleValue"] = f"{rotationAngleValue}"

    kv["angleALabel"] = f"{angleALabel}"
    kv["angleBLabel"] = f"{angleBLabel}"
    kv["angleCLabel"] = f"{angleCLabel}"    
    kv["angleDLabel"] = f"{angleDLabel}"
    kv["angleExtLabel"] = f"{angleExtLabel}"

    kv["angleCalcAValue"] = f"{angleAValue}"
    kv["angleCalcBValue"] = f"{angleBValue}"
    kv["angleCalcCValue"] = f"{angleCValue}"
    kv["angleCalcExtBValue"] = f"{angleExtBValue}"
    # kv["angleCalcBCValue"] = f"{angleBCValue}"

    return kv