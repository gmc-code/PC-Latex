"""
Module of functions to return diagram dictionary for LaTeX
"""

import random


def get_angles_in_triangle_dict():
    angleAValue = int(random.randint(0, 40) + 35)
    angleBValue = int(random.randint(0, 40) + 35)
    angleCValue = int(180 - angleAValue - angleBValue)
    # sideCValue = random.uniform(0, 1) + 3
    sideCValue = 4 + ((angleCValue - 30) / (110 - 30)) * (6 - 4)
    rotationAngleValue = int(random.randint(0, 360))

    my_lists = [["A", "B", "C"], ["F", "G", "H"], ["L", "M", "N"], ["R", "S", "T"], ["X", "Y", "Z"]]
    my_labels = random.choice(my_lists)
    gaps = r"\dotuline{~~~~~~~}"

    random.shuffle(my_labels)
    angleALabel = my_labels[0]
    angleBLabel = my_labels[1]
    angleCLabel = my_labels[2]

    kv = dict()
    kv["angleAValue"] = f"{angleAValue}"
    kv["angleBValue"] = f"{angleBValue}"
    kv["sideCValue"] = f"{sideCValue}"
    kv["rotationAngleValue"] = f"{rotationAngleValue}"

    kv["angleALabel"] = angleALabel
    kv["angleBLabel"] = angleBLabel
    kv["angleCLabel"] = angleCLabel

    kv["angleADisplayValue"] = f"${angleAValue}^\circ$"
    kv["angleBDisplayValue"] = f"${angleBValue}^\circ$"
    kv["angleCDisplayValue"] = r"$\theta^\circ$"

    kv["CalcLine1"] = rf"\text{{$\theta^\circ$}} &= 180^\circ - (\angle \text{{{angleALabel}}} + \angle \text{{{angleBLabel}}})"
    kv["CalcLine2"] = f"&= 180^\circ - ({angleAValue}^\circ + {angleBValue}^\circ)"
    kv["CalcLine3"] = f"&= 180^\circ - {angleAValue + angleBValue}^\circ"
    kv["CalcLine4"] = f"&= {angleCValue}^\circ"

    kv["CalcLine1_q"] = rf"\text{{$\theta^\circ$}} &= 180^\circ - (\angle \text{{{gaps}}} + \angle \text{{{gaps}}})"
    kv["CalcLine2_q"] = f"&= 180^\circ - ({gaps}^\circ + {gaps}^\circ)"
    kv["CalcLine3_q"] = f"&= 180^\circ - {gaps}^\circ"
    kv["CalcLine4_q"] = f"&= {gaps}^\circ"

    return kv


"""
    \angle \text{A} &= 180^\circ - (\angle \text{B} + \angle \text{C}) \\
    &= 180^\circ - (<<angleCalcBValue>>^\circ + <<angleCalcCValue>>^\circ) \\
    &= 180^\circ - <<angleCalcBCValue>>^\circ \\
    &= <<angleCalcAValue>>^\circ

"""
