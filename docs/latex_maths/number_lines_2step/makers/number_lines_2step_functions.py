"""
Module of functions to return diagram dictionary for LaTeX
"""

import random


def getprocess_dict(num, adjustment=0):
    if num is None or num == 6:
        num = random.randint(1, 5)
    match num:
        case 1:
            return go_right_dict("plus", adjustment)
        case 2:
            return go_right_dict("minus_neg", adjustment)
        case 3:
            return go_left_dict("minus", adjustment)
        case 4:
            return go_left_dict("minus_pos", adjustment)
        case 5:
            return go_left_dict("plus_neg", adjustment)


def val_in_list_exclude_zero(low, high):
    vals = [x for x in range(low, high + 1) if x not in {0}]
    return random.choice(vals)


def val_in_list_exclude_0neg1(low, high):
    # used for neg 20 to 0 where 0 becomes -10
    # exclude middle and one to left due to room for negative sign
    vals = [x for x in range(low, high + 1) if x not in {0, -1}]
    return random.choice(vals)


def val_in_list_exclude_0neg1previous(low, high, previous):
    # for left right
    vals = [x for x in range(low, high + 1) if x not in {-1, 0, previous, previous - 1, previous + 1, previous - 2, previous + 2}]
    return random.choice(vals) if vals else 0  # Return 0 if no valid numbers exist


def val_in_list_exclude_0previous(low, high, previous):
    # for left right
    vals = [x for x in range(low, high + 1) if x not in {0, previous, previous - 1, previous + 1, previous - 2, previous + 2}]
    return random.choice(vals) if vals else 0  # Return 0 if no valid numbers exist


def go_right_dict(add_style, adjustment):
    # set points
    if adjustment == -10:
        endval = val_in_list_exclude_0neg1(-7, 9)
        startval = val_in_list_exclude_0neg1(-9, endval - 2)
    else:
        endval = val_in_list_exclude_zero(-7, 9)
        startval = val_in_list_exclude_zero(-9, endval - 2)
    endval += adjustment
    startval += adjustment
    changevaltxt = endval - startval
    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    if add_style == "plus":
        kv["changevaltxt"] = r"+" + str(changevaltxt)
    else:  # minus_neg
        kv["changevaltxt"] = r"-(" + str(-changevaltxt) + ")"
    kv["equtxt"] = f"{startval}{kv['changevaltxt']} = {endval}"
    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    if add_style == "plus":
        kv["changevaltxt_q"] = r"+\qgap"
        kv["equtxt_q"] = r"\qgap + \qgap = \qgap"
    else:  # minus_neg
        kv["changevaltxt_q"] = r"-(\qgap\qgap)"
        kv["equtxt_q"] = r"\qgap - (\qgap\qgap) = \qgap"
    return kv


def go_left_dict(sub_style, adjustment):
    # set points
    if adjustment == -10:
        endval = val_in_list_exclude_0neg1(-9, 7)
        startval = val_in_list_exclude_0neg1(endval + 2, 9)
    else:
        endval = val_in_list_exclude_zero(-9, 7)
        startval = val_in_list_exclude_zero(endval + 2, 9)
    endval += adjustment
    startval += adjustment
    changevaltxt = endval - startval
    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    if sub_style == "minus":
        kv["changevaltxt"] = r"-" + str(-changevaltxt)
    elif sub_style == "minus_pos":
        kv["changevaltxt"] = r"-(+" + str(-changevaltxt) + ")"
    else:  # plus_neg
        kv["changevaltxt"] = r"+(" + str(changevaltxt) + ")"
    kv["equtxt"] = f"{startval}{kv['changevaltxt']} = {endval}"
    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    if sub_style == "minus":
        kv["changevaltxt_q"] = r"-\qgap"
        kv["equtxt_q"] = r"\qgap - \qgap = \qgap"
    elif sub_style == "minus_pos":
        kv["changevaltxt_q"] = r"-(+\qgap)"
        kv["equtxt_q"] = r"\qgap - (+\qgap) = \qgap"
    else:  # plus_neg
        kv["changevaltxt_q"] = r"+(\qgap\qgap)"
        kv["equtxt_q"] = r"\qgap + (\qgap\qgap) = \qgap"
    return kv


# ########################################################################################


def getdirections_style(num):
    directions = ["plus", "minus_neg", "minus", "minus_pos", "plus_neg"]
    return directions[num - 1]


def get_2step_process_dict(num1, num2, adjustment=0):
    if num1 is None or num1 == 6:
        num1 = random.randint(1, 5)
    if num2 is None or num2 == 6:
        num2 = random.randint(1, 5)
    processes = (num1, num2)
    direction_style1 = getdirections_style(num1)
    direction_style2 = getdirections_style(num2)
    # processes = (3,3)
    match processes:
        case (1, 1) | (1, 2) | (2, 1) | (2, 2):
            return go_right_right_dict(direction_style1, direction_style2, adjustment)
        case (1, 3) | (1, 4) | (1, 5) | (2, 3) | (2, 4) | (1, 5):
            return go_right_left_dict(direction_style1, direction_style2, adjustment)
        case (3, 1) | (3, 2) | (4, 1) | (4, 2) | (5, 1) | (5, 2):
            return go_left_right_dict(direction_style1, direction_style2, adjustment)
        case (3, 3) | (3, 4) | (3, 5) | (4, 3) | (4, 4) | (4, 5) | (5, 3) | (5, 4) | (5, 5):
            return go_left_left_dict(direction_style1, direction_style2, adjustment)


def go_right_right_dict(add_style1, add_style2, adjustment):
    # set points
    if adjustment == -10:
        endval = val_in_list_exclude_0neg1(-5, 9)
        startval = val_in_list_exclude_0neg1(-9, endval - 4)
        midval = val_in_list_exclude_0neg1(startval + 2, endval - 2)
    else:
        endval = val_in_list_exclude_zero(-5, 9)
        startval = val_in_list_exclude_zero(-9, endval - 4)
        midval = val_in_list_exclude_zero(startval + 2, endval - 2)

    endval += adjustment
    startval += adjustment
    midval += adjustment

    # positive values
    firstjumptxt = midval - startval
    secondjumptxt = endval - midval

    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    kv["midval"] = f"{midval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    kv["midvaltxt"] = f"{midval}"

    if add_style1 == "plus":
        kv["firstjumptxt"] = r"+" + str(firstjumptxt)
    else:  # minus_neg
        kv["firstjumptxt"] = r"-(" + str(-firstjumptxt) + ")"

    if add_style2 == "plus":
        kv["secondjumptxt"] = r"+" + str(secondjumptxt)
    else:  # minus_neg
        kv["secondjumptxt"] = r"-(" + str(-secondjumptxt) + ")"

    kv["equtxt"] = f"{startval}{kv['firstjumptxt']}{kv['secondjumptxt']} = {endval}"
    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    kv["midvaltxt_q"] = r"\qgap"
    if add_style1 == "plus":
        kv["firstjumptxt_q"] = r"+\qgap"
    else:  # minus_neg
        kv["firstjumptxt_q"] = r"-(\qgap\qgap)"
    if add_style2 == "plus":
        kv["secondjumptxt_q"] = r"+\qgap"
    else:  # minus_neg
        kv["secondjumptxt_q"] = r"-(\qgap\qgap)"

    kv["equtxt_q"] = rf"{kv['startvaltxt_q']}{kv['firstjumptxt_q']}{kv['secondjumptxt_q']} = {kv['endvaltxt_q']}"
    return kv


def go_left_left_dict(sub_style1, sub_style2, adjustment):
    # set points
    if adjustment == -10:
        endval = val_in_list_exclude_0neg1(-9, 5)
        startval = val_in_list_exclude_0neg1(endval + 4, 9)
        midval = val_in_list_exclude_0neg1(endval + 2, startval - 2)
    else:
        endval = val_in_list_exclude_zero(-9, 5)
        startval = val_in_list_exclude_zero(endval + 4, 9)
        midval = val_in_list_exclude_zero(endval + 2, startval - 2)

    endval += adjustment
    startval += adjustment
    midval += adjustment

    # negative values
    firstjumptxt = midval - startval
    secondjumptxt = endval - midval

    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    kv["midval"] = f"{midval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    kv["midvaltxt"] = f"{midval}"

    if sub_style1 == "minus":
        kv["firstjumptxt"] = r"-" + str(-firstjumptxt)
    elif sub_style1 == "minus_pos":
        kv["firstjumptxt"] = r"-(+" + str(-firstjumptxt) + ")"
    else:  # plus_neg
        kv["firstjumptxt"] = r"+(" + str(firstjumptxt) + ")"

    if sub_style2 == "minus":
        kv["secondjumptxt"] = r"-" + str(-secondjumptxt)
    elif sub_style2 == "minus_pos":
        kv["secondjumptxt"] = r"-(+" + str(-secondjumptxt) + ")"
    else:  # plus_neg
        kv["secondjumptxt"] = r"+(" + str(secondjumptxt) + ")"

    kv["equtxt"] = f"{startval}{kv['firstjumptxt']}{kv['secondjumptxt']} = {endval}"

    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    kv["midvaltxt_q"] = r"\qgap"
    if sub_style1 == "minus":
        kv["firstjumptxt_q"] = r"-\qgap"
    elif sub_style1 == "minus_pos":
        kv["firstjumptxt_q"] = r"-(+\qgap)"
    else:  # plus_neg
        kv["firstjumptxt_q"] = r"+(\qgap\qgap)"
    if sub_style2 == "minus":
        kv["secondjumptxt_q"] = r"-\qgap"
    elif sub_style2 == "minus_pos":
        kv["secondjumptxt_q"] = r"-(+\qgap)"
    else:  # plus_neg
        kv["secondjumptxt_q"] = r"+(\qgap\qgap)"

    kv["equtxt_q"] = rf"{kv['startvaltxt_q']}{kv['firstjumptxt_q']}{kv['secondjumptxt_q']} = {kv['endvaltxt_q']}"
    return kv


# #####################################################


def go_right_left_dict():
    return None


def go_left_right_dict(sub_style1, add_style2, adjustment):
    # set points
    if adjustment == -10:
        startval = val_in_list_exclude_0neg1(-7, 9)
        midval = val_in_list_exclude_0neg1(-9, startval - 3)
        endval = val_in_list_exclude_0neg1(midval + 3, 9)
    else:
        startval = val_in_list_exclude_zero(-7, 9)
        midval = val_in_list_exclude_zero(-9, startval - 3)
        endval = val_in_list_exclude_0previous(midval + 3, 9, startval)

    endval += adjustment
    startval += adjustment
    midval += adjustment

    # negative values
    firstjumptxt = midval - startval
    # positive value
    secondjumptxt = endval - midval

    kv = dict()
    kv["endval"] = f"{endval}"
    kv["startval"] = f"{startval}"
    kv["midval"] = f"{midval}"
    # answers
    kv["endvaltxt"] = f"{endval}"
    kv["startvaltxt"] = f"{startval}"
    kv["midvaltxt"] = f"{midval}"

    if sub_style1 == "minus":
        kv["firstjumptxt"] = r"-" + str(-firstjumptxt)
    elif sub_style1 == "minus_pos":
        kv["firstjumptxt"] = r"-(+" + str(-firstjumptxt) + ")"
    else:  # plus_neg
        kv["firstjumptxt"] = r"+(" + str(firstjumptxt) + ")"

    if add_style2 == "plus":
        kv["secondjumptxt"] = r"+" + str(secondjumptxt)
    else:  # minus_neg
        kv["secondjumptxt"] = r"-(" + str(-secondjumptxt) + ")"

    kv["equtxt"] = f"{startval}{kv['firstjumptxt']}{kv['secondjumptxt']} = {endval}"

    # _question
    kv["endvaltxt_q"] = r"\qgap"
    kv["startvaltxt_q"] = r"\qgap"
    kv["midvaltxt_q"] = r"\qgap"
    if sub_style1 == "minus":
        kv["firstjumptxt_q"] = r"-\qgap"
    elif sub_style1 == "minus_pos":
        kv["firstjumptxt_q"] = r"-(+\qgap)"
    else:  # plus_neg
        kv["firstjumptxt_q"] = r"+(\qgap\qgap)"

    if add_style2 == "plus":
        kv["secondjumptxt_q"] = r"+\qgap"
    else:  # minus_neg
        kv["secondjumptxt_q"] = r"-(\qgap\qgap)"

    kv["equtxt_q"] = rf"{kv['startvaltxt_q']}{kv['firstjumptxt_q']}{kv['secondjumptxt_q']} = {kv['endvaltxt_q']}"
    return kv
