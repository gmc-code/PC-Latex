"""
Module of functions to return diagram dictionary for LaTeX
# escape {} in f strings by doubling them up {{}}
"""

import random


def get_offset():
    off_numbers = [-3, -2, -1, 1, 2, 3]
    return random.choice(off_numbers)


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
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na - nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
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
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
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
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
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
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        # offset a multiple such that
        xval = xsol + (get_offset() * nx)
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


def val_in_list_exclude(low, high, exclude):
    # random 2 step: avoid xx, x/, /x, //, ++, --, +-, -+
    vals = list(range(low, high + 1))
    if exclude in vals:
        if exclude in [1, 2]:
            vals.remove(1)
            vals.remove(2)
        elif exclude in [3, 4]:
            vals.remove(3)
            vals.remove(4)
    return random.choice(vals)


def get_2step_process_dict(num1, num2):
    if num1 is None or num1 == 5:
        num1 = random.randint(1, 4)
    if num2 is None or num2 == 5:
        num2 = random.randint(1, 4)
        # num2 = val_in_list_exclude(1, 4, num1)
    processes = (num1, num2)
    # processes = (3,3)
    match processes:
        case (1, 1):
            return add_add_dict()
        case (1, 2):
            return add_sub_dict()
        case (1, 3):
            return add_times_dict()
        case (1, 4):
            return add_div_dict()
        case (2, 1):
            return sub_add_dict()
        case (2, 2):
            return sub_sub_dict()
        case (2, 3):
            return sub_times_dict()
        case (2, 4):
            return sub_div_dict()
        case (3, 1):
            return times_add_dict()
        case (3, 2):
            return times_sub_dict()
        case (3, 3):
            return times_times_dict()
        case (3, 4):
            return times_div_dict()
        case (4, 1):
            return div_add_dict()
        case (4, 2):
            return div_sub_dict()
        case (4, 3):
            return div_times_dict()
        case (4, 4):
            return div_div_dict()
        case _:
            return add_add_dict()


def add_add_dict():
    # x + nx + mx = na
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na - nx - mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"x + {nx} + {mx} = {na}"
    kv["LHS"] = f"x + {nx} + {mx}"
    kv["LHSsub"] = f"{xval} + {nx} + {mx}"
    kv["LHSval"] = f"{xval + nx + mx} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def add_sub_dict():
    # bc = nx + na - nb
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    bb = nx + na
    if bb > 10:
        nb = random.randint(1, 10)
    else:
        nb = random.randint(1, bb)
    bc = bb - nb

    # x + nx - mx = na
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na - nx + mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"x + {nx} - {mx} = {na}"
    kv["LHS"] = f"x + {nx} - {mx}"
    kv["LHSsub"] = f"{xval} + {nx} - {mx}"
    kv["LHSval"] = f"{xval + nx - mx} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def add_times_dict():
    # xsol = x; xval is test val
    # mx * (x + nx) = na
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    xsol = random.randint(1, 10)
    na = mx * (xsol + nx)
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"{mx}(x + {nx}) = {na}"
    kv["LHS"] = f"{mx}(x + {nx})"
    kv["LHSsub"] = f"{mx} \\times({xval} + {nx})"
    kv["LHSval"] = f"{mx * (xval + nx)} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def add_div_dict():
    # xsol = x; xval is test val
    # (x + nx)/mx = na
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    na = random.randint(1, 10)
    xsol = (na * mx) - nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * mx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x + {nx}}}{{{mx}}} = {na}"
    kv["LHS"] = f"\\frac{{x + {nx}}}{{{mx}}}"
    kv["LHSsub"] = f"\\frac{{{xval} + {nx}}}{{{mx}}}"
    kv["LHSval"] = f"{(xval + nx) / mx}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def sub_add_dict():
    # x - nx + mx = na
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na + nx - mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"x - {nx} + {mx} = {na}"
    kv["LHS"] = f"x - {nx} + {mx}"
    kv["LHSsub"] = f"{xval} - {nx} + {mx}"
    kv["LHSval"] = f"{xval - nx + mx} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def sub_sub_dict():
    # x - nx - mx = na
    # xsol = x; xval is test val
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = na + nx + mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"x - {nx} - {mx} = {na}"
    kv["LHS"] = f"x + {nx} - {mx}"
    kv["LHSsub"] = f"{xval} - {nx} - {mx}"
    kv["LHSval"] = f"{xval - nx - mx} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def sub_times_dict():
    # xsol = x; xval is test val
    # mx * (x - nx) = na
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    xsol = random.randint(1, 10)
    na = mx * (xsol - nx)
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"{mx}(x - {nx}) = {na}"
    kv["LHS"] = f"{mx}(x - {nx})"
    kv["LHSsub"] = f"{mx} \\times({xval} - {nx})"
    kv["LHSval"] = f"{mx * (xval - nx)} "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def sub_div_dict():
    # xsol = x; xval is test val
    # (x - nx)/mx = na
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    na = random.randint(1, 10)
    xsol = (na * mx) + nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * mx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x - {nx}}}{{{mx}}} = {na}"
    kv["LHS"] = f"\\frac{{x - {nx}}}{{{mx}}}"
    kv["LHSsub"] = f"\\frac{{{xval} - {nx}}}{{{mx}}}"
    kv["LHSval"] = f"{(xval - nx) / mx}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def times_add_dict():
    # xsol = x; xval is test val
    # (x * nx) + mx = na
    nx = random.randint(2, 10)
    mx = random.randint(1, 10)
    xsol = random.randint(1, 10)
    na = (xsol * nx) + mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"{nx}x + {mx} = {na}"
    kv["LHS"] = f"{nx}x + {mx}"
    kv["LHSsub"] = f"{nx} \\times{xval} + {mx}"
    kv["LHSval"] = f"{(xval * nx) + mx } "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def times_sub_dict():
    # xsol = x; xval is test val
    # (x * nx) - mx = na
    nx = random.randint(2, 10)
    mx = random.randint(1, 10)
    xsol = random.randint(1, 10)
    na = (xsol * nx) - mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"{nx}x - {mx} = {na}"
    kv["LHS"] = f"{nx}x - {mx}"
    kv["LHSsub"] = f"{nx} \\times{xval} - {mx}"
    kv["LHSval"] = f"{(xval * nx) - mx } "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def times_times_dict():
    # xsol = x; xval is test val
    # x * nx * mx = na
    nx = random.randint(2, 10)
    mx = random.randint(2, 10)
    xsol = random.randint(1, 10)
    na = xsol * nx * mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + get_offset()
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"{nx}x \\times {mx} = {na}"
    kv["LHS"] = f"{nx}x \\times {mx}"
    kv["LHSsub"] = f"{nx} \\times{xval} \\times {mx}"
    kv["LHSval"] = f"{xval * nx * mx } "
    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def times_div_dict():
    # xsol = x; xval is test val
    # (x * nx)/mx = na
    nx = random.randint(2, 10)
    xsol = random.randint(2, 10)
    mx_candidates = [i for i in range(2, 11) if (xsol * nx) % i == 0]
    mx = random.choice(mx_candidates)
    na = (xsol * nx) // mx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * mx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{{nx}x}}{{{mx}}} = {na}"
    kv["LHS"] = f"\\frac{{{nx}x}}{{{mx}}}"
    kv["LHSsub"] = f"\\frac{{{nx} \\times{xval}}}{{{mx}}}"
    kv["LHSval"] = f"{(xval * nx) / mx}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def div_add_dict():
    # xsol = x; xval is test val
    # x/nx + mx = na
    nx = random.randint(2, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = (na - mx) * nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * nx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x}}{{{nx}}} + {mx} = {na}"
    kv["LHS"] = f"\\frac{{x}}{{{nx}}} + {mx}"
    kv["LHSsub"] = f"\\frac{{{xval}}}{{{nx}}} + {mx}"
    kv["LHSval"] = f"{(xval // nx) + mx}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def div_sub_dict():
    # xsol = x; xval is test val
    # x/nx - mx = na
    nx = random.randint(2, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xsol = (na + mx) * nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * nx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x}}{{{nx}}} - {mx} = {na}"
    kv["LHS"] = f"\\frac{{x}}{{{nx}}} - {mx}"
    kv["LHSsub"] = f"\\frac{{{xval}}}{{{nx}}} - {mx}"
    kv["LHSval"] = f"{(xval // nx) - mx}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def div_times_dict():
    # xsol = x; xval is test val
    # (x / nx) * mx = na
    mx = random.randint(2, 10)
    xsol = random.randint(2, 10)
    nx_candidates = [i for i in range(2, 11) if (xsol * mx) % i == 0]
    nx = random.choice(nx_candidates)
    na = (xsol * mx) // nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * nx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x}}{{{nx}}} \\times {mx} = {na}"
    kv["LHS"] = f"\\frac{{x}}{{{nx}}} \\times {mx}"
    kv["LHSsub"] = f"\\frac{{{xval}}}{{{nx}}} \\times {mx}"
    kv["LHSval"] = f"{(xval * mx) // nx}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv


def div_div_dict():
    # bc = (nx / na) / nb
    # escape {} in f strings by doubling them up {{}}
    # xsol = x; xval is test val
    # (x / nx) / mx = na
    mx = random.randint(2, 7)
    nx = random.randint(2, 7)
    na = random.randint(2, 7)
    xsol = na * mx * nx
    #
    kv = dict()
    if random.randint(1, 10) > 6:
        xval = xsol + (get_offset() * nx)
        kv["side_equality"] = r"\neq"
        kv["is_a_sol"] = "is not "
    else:
        xval = xsol
        kv["side_equality"] = "="
        kv["is_a_sol"] = "is "
    #
    kv["pro_value"] = f"x = {xval}"
    kv["equation"] = f"\\frac{{x}}{{{nx}}} \\times \\frac{{1}}{{{mx}}} = {na}"
    kv["LHS"] = f"\\frac{{x}}{{{nx}}} \\times \\frac{{1}}{{{mx}}}"
    kv["LHSsub"] = f"\\frac{{{xval}}}{{{nx}}} \\times \\frac{{1}}{{{mx}}}"
    kv["LHSval"] = f"{xval // (mx * nx)}"

    kv["LHSq"] = f""
    kv["LHSsubq"] = f""
    kv["LHSvalq"] = f""
    kv["RHS"] = f"{na}"
    kv["RHSq"] = f""
    kv["side_equalityq"] = r"\dotuline{\hspace{5mm}}"
    kv["is_a_solq"] = r"\dotuline{\hspace{12mm}}"
    return kv
