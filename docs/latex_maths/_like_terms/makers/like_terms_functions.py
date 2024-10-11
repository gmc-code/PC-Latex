"""
Module of functions to return diagram dictionary for LaTeX
# escape {} in f strings by doubling them up {{}}
"""
import random


def get_1step_process_dict(num):
    if num is None or num == 5:
        num = random.randint(1, 4)
    match num:
        case 1:
            return add_dict()
        case 2:
            return sub_dict()
        case 3:
            return times_dict()
        case 4:
            return div_dict()



def add_dict():
    # x + nx = na
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na - nx
    kv = dict()
    kv["line1_LHS"] = f"x + {nx}"
    kv["line2_LHS"] = f"x + {nx} - {nx}"
    kv["line2_LHSq"] = f"x + {nx} - {r'\dotuline{\hspace{5mm}}'}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} - {nx}"
    kv["line2_RHSq"] = f"{na} - {r'\dotuline{\hspace{5mm}}'}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{r'\dotuline{\hspace{5mm}}'}"
    return kv


def sub_dict():
    # x - nx = na
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na + nx
    kv = dict()
    kv["line1_LHS"] = f"x - {nx}"
    kv["line2_LHS"] = f"x - {nx} + {nx}"
    kv["line2_LHSq"] = f"x - {nx} + {r'\dotuline{\hspace{5mm}}'}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} + {nx}"
    kv["line2_RHSq"] = f"{na} + {r'\dotuline{\hspace{5mm}}'}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{r'\dotuline{\hspace{5mm}}'}"
    return kv


def times_dict():
    # x * nx = na
    nx = random.randint(2, 10)
    xval = random.randint(2, 10)
    na = xval * nx

    kv = dict()
    kv["line1_LHS"] = f"{nx}x"
    kv["line2_LHS"] = f"\\frac{{{nx}x}}{{{nx}}}"
    #  kv["line2_LHSq"] = f"\\frac{{{nx}x}}{{{r'\dotuline{\hspace{5mm}}'}}}"

    kv["line2_LHSq"] = f"\\frac{{{nx}x}}{{{r'\dotuline{\hspace{5mm}}'}}}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"\\frac{{{na}}}{{{nx}}}"
    kv["line2_RHSq"] = f"\\frac{{{na}}}{{{r'\dotuline{\hspace{5mm}}'}}}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{r'\dotuline{\hspace{5mm}}'}"
    return kv


def div_dict():
    # x / nx = na
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    xval = na * nx

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["line2_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{nx}"
    kv["line2_LHSq"] = f"\\frac{{x}}{{{nx}}} \\times{{{r'\dotuline{\hspace{5mm}}'}}}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} \\times{nx}"
    kv["line2_RHSq"] = f"{na} \\times{{{r'\dotuline{\hspace{5mm}}'}}}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{r'\dotuline{\hspace{5mm}}'}"
    return kv



# ############################################
