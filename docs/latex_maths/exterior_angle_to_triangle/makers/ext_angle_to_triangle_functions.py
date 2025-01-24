"""
Module of functions to return diagram dictionary for LaTeX
"""
import random



def get_ext_angle_to_triangle_dict(unknown_ang_num):
    if unknown_ang_num is None or unknown_ang_num == 4:
        unknown_ang_num = random.randint(1, 3)

    angleAValue = int(random.randint(0,40)+25)
    angleBValue = int(random.randint(0,40)+25)
    angleCValue = int(180-angleAValue-angleBValue)
    angleExtBValue = int(180-angleBValue)

    # angleBCValue = int(angleBValue+angleCValue)
    sideCValue = random.uniform(0, 1) + 3
    sideDValue = sideCValue + 1

    rotationAngleValue = int(random.randint(0,360))
    # gap_to_fill = "\\dotuline{~~~~~~~}"

    vertices_lists = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["J", "K", "L", "M"], ["Q", "R", "S", "T"], ["X", "Y", "Z", "W"]]
     vertices_labels = random.choice(vertices_lists)
   # Shuffle the first 3 elements, leaving the last one in place
    shuffled_part =  vertices_labels[:3]  # Get the first three elements
    random.shuffle(shuffled_part)  # Shuffle them
    # Reassign the shuffled elements back, leaving the last element unchanged
     vertices_labels[:3] = shuffled_part

    angleALabel =  vertices_labels[0]
    angleBLabel =  vertices_labels[1]
    angleCLabel =  vertices_labels[2]
    angleDLabel =  vertices_labels[3]
    angleExtBLabel = angleDLabel + angleBLabel + angleCLabel

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
    kv["angleExtBLabel"] = f"{angleExtBLabel}"

    kv["angleAValueDisplay"] = f"{angleAValue}"
    kv["angleBValueDisplay"] = f"{angleBValue}"
    kv["angleCValueDisplay"] = f"{angleCValue}"
    kv["angleExtBValueDisplay"] = f"{angleExtBValue}"

    match unknown_ang_num:
        case 1:
            kv["process"] = f"-"
            kv["angleAValueDisplay"] = f"\\theta"
            kv["angleLabel1"] = f"{angleALabel}"
            kv["angleLabel2"] = f"{angleExtBLabel}"
            kv["angleLabel3"] = f"{angleCLabel}"
            kv["angleValue1"] = f"{angleAValue}"
            kv["angleValue2"] = f"{angleExtBValue}"
            kv["angleValue3"] = f"{angleCValue}"
        case 2:
            kv["process"] = f"-"
            kv["angleCValueDisplay"] = f"\\theta"
            kv["angleLabel1"] = f"{angleCLabel}"
            kv["angleLabel2"] = f"{angleExtBLabel}"
            kv["angleLabel3"] = f"{angleALabel}"
            kv["angleValue1"] = f"{angleCValue}"
            kv["angleValue2"] = f"{angleExtBValue}"
            kv["angleValue3"] = f"{angleAValue}"
        case 3:
            kv["process"] = f"+"
            kv["angleExtBValueDisplay"] = f"\\theta"
            kv["angleLabel1"] = f"{angleExtBLabel}"
            kv["angleLabel2"] = f"{angleALabel}"
            kv["angleLabel3"] = f"{angleCLabel}"
            kv["angleValue1"] = f"{angleExtBValue}"
            kv["angleValue2"] = f"{angleAValue}"
            kv["angleValue3"] = f"{angleCValue}"

    return kv