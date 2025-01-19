import random

def get_angles_in_iso_triangle_dict(unknown_ang_num):
    # 1 for unique C, 2 for paired A/B, 3 random; unknown_ang_num
    if unknown_ang_num is None or unknown_ang_num == 3:
        unknown_ang_num = random.randint(1, 2)

    angleAValue = int(random.randint(0, 40) + 25)
    angleBValue = angleAValue
    angleCValue = int(180 - angleAValue - angleBValue)
    angleABValue = int(angleAValue + angleBValue)
    sideCValue = random.uniform(0, 1) + 3
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

    # unknowns, 1C, 2AorB
    match unknown_ang_num:
        case 1:
            # C theta
            showAorB = random.randint(1, 2)
            if showAorB == 1:
                # show A
                kv["angleADisplayValue"] = f"${angleAValue}^\circ$"
                kv["angleBDisplayValue"] = ""
                kv["angleCDisplayValue"] = r"$\theta^\circ$"
            else:
                # show B
                kv["angleADisplayValue"] = ""
                kv["angleBDisplayValue"] = f"${angleBValue}^\circ$"
                kv["angleCDisplayValue"] = r"$\theta^\circ$"

            kv["CalcLine1"] = fr"\text{{$\theta^\circ$}} &= 180^\circ - (\angle \text{{{angleALabel}}} + \angle \text{{{angleBLabel}}})"
            kv["CalcLine2"] = f"&= 180^\circ - ({angleAValue}^\circ + {angleBValue}^\circ)"
            kv["CalcLine3"] = f"&= 180^\circ - {angleABValue}^\circ"
            kv["CalcLine4"] = f"&= {angleCValue}^\circ"
            kv["CalcLine1_q"] = fr"\text{{$\theta^\circ$}} &= 180^\circ - (\angle \text{{{gaps}}} + \angle \text{{{gaps}}})"
            kv["CalcLine2_q"] = f"&= 180^\circ - ({gaps}^\circ + {gaps}^\circ)"
            kv["CalcLine3_q"] = f"&= 180^\circ - {gaps}^\circ"
            kv["CalcLine4_q"] = f"&= {gaps}^\circ"

        case 2:
            # A or B theta
            unkownAorB = random.randint(1, 2)
            if unkownAorB == 1:
                # theta is A
                kv["angleADisplayValue"] = r"$\theta^\circ$"
                kv["angleBDisplayValue"] = ""
                kv["angleCDisplayValue"] = f"${angleCValue}^\circ$"
            else:
                #  theta is  B
                kv["angleADisplayValue"] = ""
                kv["angleBDisplayValue"] = r"$\theta^\circ$"
                kv["angleCDisplayValue"] = f"${angleCValue}^\circ$"

            kv["CalcLine1"] = fr"\text{{$\theta^\circ$}} &= \frac{{(180^\circ - \angle \text{{{angleCLabel}}})}}{{2}}"
            kv["CalcLine2"] = f"&= \\frac{{(180^\circ - {angleCValue}^\circ)}}{{2}}"
            kv["CalcLine3"] = f"&= \\frac{{{180-angleCValue}^\circ}}{{2}}"
            kv["CalcLine4"] = f"&= {angleAValue}^\circ"
            kv["CalcLine1_q"] = fr"\text{{$\theta^\circ$}} &= \frac{{(180^\circ - \angle \text{{{gaps}}})}}{{2}}"
            kv["CalcLine2_q"] = f"&= \\frac{{(180^\circ - {gaps}^\circ)}}{{2}}"
            kv["CalcLine3_q"] = f"&= \\frac{{{gaps}^\circ}}{{2}}"
            kv["CalcLine4_q"] = f"&= {gaps}^\circ"

    return kv
