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


import random

off_numbers = [-3, -2, -1, 1, 2, 3]


def add_dict():
    # x + nx = na
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na - nx
    #
    kv = dict()
    if random.randint(1, 10) > 5:
        xval = xsol + random.choice(off_numbers)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #

    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"x + {nx} = {na}"
    kv["LHS"] = f"x + {nx}"
    kv["LHSsub"] = f"{xval} + {nx}"
    kv["LHSval"] = f"{xval + nx} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


"""
kv["pro_value"]   x=4
kv["equation"]  x + 5 = 9
kv["LHS"]
kv["LHSsub"]
kv["LHSval"]

kv["side_equality"]
kv["is_a_sol"]
"""


def sub_dict():
    # x - nx = na
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na + nx
    #
    kv = dict()
    if random.randint(1, 10) > 5:
        xval = xsol + random.choice(off_numbers)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #

    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"x - {nx} = {na}"
    kv["LHS"] = f"x - {nx}"
    kv["LHSsub"] = f"{xval} - {nx}"
    kv["LHSval"] = f"{xval - nx} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def times_dict():
    # xsol = x; xval is test val
    # x * nx = na
    nx = random.randint(2, 10)
    xsol = random.randint(2, 10)
    na = xsol * nx
    #
    kv = dict()
    if random.randint(1, 10) > 5:
        xval = xsol + random.choice(off_numbers)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"{nx}x = {na}"
    kv["LHS"] = f"{nx}x"
    kv["LHSsub"] = f"{nx} \\times{xval}"
    kv["LHSval"] = f"{nx * xval} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def div_dict():
    # xsol = x; xval is test val
    # x / nx = na
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    xsol = na * nx


    kv = dict()
    if random.randint(1, 10) > 5:
        xval = xsol + random.choice(off_numbers)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
        if xval % nx == 0:
            xval_div_nx = int(xval / nx)
        else:
            xval_div_nx = round(xval / nx, 3)
        kv["LHSval"] = f"{xval_div_nx}"
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
        kv["LHSval"] = f"{na}"  # to avoid ".0" for float
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x}}{{{nx}}} = {na}"
    kv["LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["LHSsub"] = f"\\frac{{{xval}}}{{{nx}}}"
    # kv["LHSval"] = f"{xval / nx}"  # see above
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


# ############################################
