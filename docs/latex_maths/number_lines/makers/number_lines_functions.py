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
    vals = list(range(low, high + 1))
    if 0 in vals:
        vals.remove(0)
    return random.choice(vals)


def val_in_list_exclude_neg20to0(low, high):
    # exclude middle and one to left due to room for negative sign
    vals = list(range(low, high + 1))
    if 0 in vals:
        vals.remove(0)
    if -1 in vals:
        vals.remove(-1)
    return random.choice(vals)


def go_right_dict(add_style, adjustment):
    # set points
    if adjustment == -10:
        endval = val_in_list_exclude_neg20to0(-7, 9)
        startval = val_in_list_exclude_neg20to0(-9, endval - 2)
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
        endval = val_in_list_exclude_neg20to0(-9, 7)
        startval = val_in_list_exclude_neg20to0(endval + 2, 9)
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



