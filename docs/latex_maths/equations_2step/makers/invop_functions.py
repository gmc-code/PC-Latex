"""
Module of functions to return diagram dictionary for LaTeX
# escape {} in f strings by doubling them up {{}}
"""
import random

gap = r'\dotuline{\hspace{5mm}}'

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
    kv["line2_LHSq"] = f"x + {nx} - {gap}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} - {nx}"
    kv["line2_RHSq"] = f"{na} - {gap}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{gap}"
    return kv


def sub_dict():
    # x - nx = na
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na + nx
    kv = dict()
    kv["line1_LHS"] = f"x - {nx}"
    kv["line2_LHS"] = f"x - {nx} + {nx}"
    kv["line2_LHSq"] = f"x - {nx} + {gap}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} + {nx}"
    kv["line2_RHSq"] = f"{na} + {gap}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{gap}"
    return kv


def times_dict():
    # x * nx = na
    nx = random.randint(2, 10)
    na = nx * random.randint(2, 10)
    xval = int(na / nx)
    kv = dict()
    kv["line1_LHS"] = f"{nx}x"
    kv["line2_LHS"] = f"\\frac{{{nx}x}}{{{nx}}}"
    kv["line2_LHSq"] = f"\\frac{{{nx}x}}{{{gap}}}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"\\frac{{{na}}}{{{nx}}}"
    kv["line2_RHSq"] = f"\\frac{{{na}}}{{{gap}}}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{gap}"
    return kv


def div_dict():
    # x / nx = na
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    xval = na * nx
    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["line2_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{nx}"
    kv["line2_LHSq"] = f"\\frac{{x}}{{{nx}}} \\times{{{gap}}}"
    kv["line3_LHS"] = f"x"
    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} \\times{nx}"
    kv["line2_RHSq"] = f"{na} \\times{{{gap}}}"
    kv["line3_RHS"] = f"{xval}"
    kv["line3_RHSq"] = f"{gap}"
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
        num2 = val_in_list_exclude(1, 4, num1)
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
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na - nx - mx

    kv = dict()
    kv["line1_LHS"] = f"x + {nx} + {mx}"
    kv["line2_LHS"] = f"x + {nx} - {nx} + {mx}"
    kv["line2_LHSq"] = f"x + {nx} - {gap} + {mx}"
    kv["line3_LHS"] = f"x + {mx}"
    kv["line4_LHS"] = f"x + {mx} - {mx}"
    kv["line4_LHSq"] = f"x + {mx} - {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} - {nx}"
    kv["line2_RHSq"] = f"{na} - {gap}"
    kv["line3_RHS"] = f"{na - nx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na - nx} - {mx}"
    kv["line4_RHSq"] = f"{gap} - {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def add_sub_dict():
    # x + nx - mx = na
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na - nx + mx

    kv = dict()
    kv["line1_LHS"] = f"x + {nx} - {mx}"
    kv["line2_LHS"] = f"x + {nx} - {nx} - {mx}"
    kv["line2_LHSq"] = f"x + {nx} - {gap} - {mx}"
    kv["line3_LHS"] = f"x - {mx}"
    kv["line4_LHS"] = f"x - {mx} + {mx}"
    kv["line4_LHSq"] = f"x - {mx} + {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} - {nx}"
    kv["line2_RHSq"] = f"{na} - {gap}"
    kv["line3_RHS"] = f"{na - nx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na - nx} + {mx}"
    kv["line4_RHSq"] = f"{gap} + {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def add_times_dict():
    # (x + nx) * mx = na
    xval = random.randint(1, 10)
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    na = (xval + nx) * mx

    kv = dict()
    kv["line1_LHS"] = f"{mx}(x + {nx})"
    kv["line2_LHS"] = f"\\frac{{{mx}(x+{nx})}}{{{mx}}}"
    kv["line2_LHSq"] =  f"\\frac{{{mx}(x+{nx})}}{{{gap}}}"
    kv["line3_LHS"] = f"x + {nx}"
    kv["line4_LHS"] = f"x + {nx} - {nx}"
    kv["line4_LHSq"] = f"x + {nx} - {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"\\frac{{{na}}}{{{mx}}}"
    kv["line2_RHSq"] = f"\\frac{{{na}}}{{{gap}}}"
    kv["line3_RHS"] = f"{int(na / mx)}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{int(na / mx)} - {nx}"
    kv["line4_RHSq"] = f"{gap} - {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def add_div_dict():
   # (x + nx) / mx = na
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    na = random.randint(1, 10)
    xval = na * mx - nx

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x + {nx}}}{{{mx}}}"
    kv["line2_LHS"] = f"\\frac{{x + {nx}}}{{{mx}}} \\times{mx}"
    kv["line2_LHSq"] = f"\\frac{{x + {nx}}}{{{mx}}} \\times{gap}"
    kv["line3_LHS"] = f"x + {nx}"
    kv["line4_LHS"] = f"x + {nx} - {nx}"
    kv["line4_LHSq"] = f"x + {nx} - {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} \\times{mx}"
    kv["line2_RHSq"] = f"{na} \\times{gap}"
    kv["line3_RHS"] = f"{na * mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na * mx} - {nx}"
    kv["line4_RHSq"] = f"{gap} - {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv



def sub_add_dict():
    # x - nx + mx = na
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na - nx + mx

    kv = dict()
    kv["line1_LHS"] = f"x - {nx} + {mx}"
    kv["line2_LHS"] = f"x - {nx} + {nx} + {mx}"
    kv["line2_LHSq"] = f"x - {nx} + {gap} + {mx}"
    kv["line3_LHS"] = f"x + {mx}"
    kv["line4_LHS"] = f"x + {mx} - {mx}"
    kv["line4_LHSq"] = f"x + {mx} - {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} + {nx}"
    kv["line2_RHSq"] = f"{na} + {gap}"
    kv["line3_RHS"] = f"{na + nx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na + nx} - {mx}"
    kv["line4_RHSq"] = f"{gap} - {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv

def sub_sub_dict():
    # x - nx - mx = na
    nx = random.randint(1, 10)
    mx = random.randint(1, 10)
    na = random.randint(1, 10)
    xval = na + nx + mx

    kv = dict()
    kv["line1_LHS"] = f"x - {nx} - {mx}"
    kv["line2_LHS"] = f"x - {nx} + {nx} - {mx}"
    kv["line2_LHSq"] = f"x - {nx} + {gap} - {mx}"
    kv["line3_LHS"] = f"x - {mx}"
    kv["line4_LHS"] = f"x - {mx} + {mx}"
    kv["line4_LHSq"] = f"x - {mx} + {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} + {nx}"
    kv["line2_RHSq"] = f"{na} + {gap}"
    kv["line3_RHS"] = f"{na + nx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na + nx} + {mx}"
    kv["line4_RHSq"] = f"{gap} + {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv

def sub_times_dict():
    # (x - nx) * mx = na
    xval = random.randint(1, 10)
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    na = (xval - nx) * mx

    kv = dict()
    kv["line1_LHS"] = f"{mx}(x - {nx})"
    kv["line2_LHS"] = f"\\frac{{{mx}(x-{nx})}}{{{mx}}}"
    kv["line2_LHSq"] =  f"\\frac{{{mx}(x-{nx})}}{{{gap}}}"
    kv["line3_LHS"] = f"x - {nx}"
    kv["line4_LHS"] = f"x - {nx} + {nx}"
    kv["line4_LHSq"] = f"x - {nx} + {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"\\frac{{{na}}}{{{mx}}}"
    kv["line2_RHSq"] = f"\\frac{{{na}}}{{{gap}}}"
    kv["line3_RHS"] = f"{int(na / mx)}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{int(na / mx)} + {nx}"
    kv["line4_RHSq"] = f"{gap} + {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv

def sub_div_dict():
    # (x - nx) / mx = na
    nx = random.randint(1, 10)
    mx = random.randint(2, 10)
    na = random.randint(1, 10)
    xval = nx * mx + nx

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x - {nx}}}{{{mx}}}"
    kv["line2_LHS"] = f"\\frac{{x - {nx}}}{{{mx}}} \\times{mx}"
    kv["line2_LHSq"] = f"\\frac{{x - {nx}}}{{{mx}}} \\times{gap}"
    kv["line3_LHS"] = f"x - {nx}"
    kv["line4_LHS"] = f"x - {nx} + {nx}"
    kv["line4_LHSq"] = f"x - {nx} + {gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} \\times{mx}"
    kv["line2_RHSq"] = f"{na} \\times{gap}"
    kv["line3_RHS"] = f"{na * mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na * mx} + {nx}"
    kv["line4_RHSq"] = f"{gap} + {gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def times_add_dict():
    # nx * x + mx = na
    xval = random.randint(1, 10)
    nx = random.randint(2, 10)
    mx = random.randint(1, 10)
    na = (xval * nx) + mx

    kv = dict()
    kv["line1_LHS"] = f"{nx}x + {mx}"
    kv["line2_LHS"] = f"{nx}x + {mx} - {mx}"
    kv["line2_LHSq"] =  f"{nx}x + {mx} - {gap}"
    kv["line3_LHS"] = f"{nx}x"
    kv["line4_LHS"] = f"\\frac{{{nx}x}}{{{nx}}}"
    kv["line4_LHSq"] = f"\\frac{{{nx}x}}{{{gap}}}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} - {mx}"
    kv["line2_RHSq"] = f"{na} - {gap}"
    kv["line3_RHS"] = f"{na - mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"\\frac{{{na - mx}}}{{{nx}}}"
    kv["line4_RHSq"] = f"\\frac{{{gap}}}{{{gap}}}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def times_sub_dict():
    # nx * x - mx = na
    xval = random.randint(1, 10)
    nx = random.randint(2, 10)
    mx = random.randint(1, 10)
    na = (xval * nx) - mx

    kv = dict()
    kv["line1_LHS"] = f"{nx}x - {mx}"
    kv["line2_LHS"] = f"{nx}x - {mx} + {mx}"
    kv["line2_LHSq"] =  f"{nx}x - {mx} + {gap}"
    kv["line3_LHS"] = f"{nx}x"
    kv["line4_LHS"] = f"\\frac{{{nx}x}}{{{nx}}}"
    kv["line4_LHSq"] = f"\\frac{{{nx}x}}{{{gap}}}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} + {mx}"
    kv["line2_RHSq"] = f"{na} + {gap}"
    kv["line3_RHS"] = f"{na + mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"\\frac{{{na + mx}}}{{{nx}}}"
    kv["line4_RHSq"] = f"\\frac{{{gap}}}{{{gap}}}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def times_times_dict():
    # nx * x * mx = na
    xval = random.randint(1, 10)
    nx = random.randint(2, 10)
    mx = random.randint(2, 10)
    na = xval * nx * mx

    kv = dict()
    kv["line1_LHS"] = f"{nx}x \\times{mx}"
    kv["line2_LHS"] = f"\\frac{{{nx}x \\times{mx}}}{{{mx}}}"
    kv["line2_LHSq"] =  f"\\frac{{{nx}x \\times{mx}}}{{{gap}}}"
    kv["line3_LHS"] = f"{nx}x"
    kv["line4_LHS"] = f"\\frac{{{nx}x}}{{{nx}}}"
    kv["line4_LHSq"] = f"\\frac{{{nx}x}}{{{gap}}}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"\\frac{{{na}}}{{{mx}}}"
    kv["line2_RHSq"] = f"\\frac{{{na}}}{{{gap}}}"
    kv["line3_RHS"] = f"{int(na / mx)}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"\\frac{{{int(na / mx)}}}{{{nx}}}"
    kv["line4_RHSq"] = f"\\frac{{{gap}}}{{{gap}}}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv

def times_div_dict():
    # (nx * x) / mx = na
    xval = random.randint(1, 10)
    mx = random.randint(2, 4)
    nx = mx * random.randint(2, 5)
    na = int((nx * xval) / mx)

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{{nx}x}}{{{mx}}}"
    kv["line2_LHS"] = f"\\frac{{{nx}x}}{{{mx}}} \\times{mx}"
    kv["line2_LHSq"] =  f"\\frac{{{nx}x}}{{{mx}}} \\times{gap}"
    kv["line3_LHS"] = f"{nx}x"
    kv["line4_LHS"] = f"\\frac{{{nx}x}}{{{nx}}}"
    kv["line4_LHSq"] = f"\\frac{{{nx}x}}{{{gap}}}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na}\\times{mx}"
    kv["line2_RHSq"] = f"{na}\\times{gap}"
    kv["line3_RHS"] = f"{na * mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"\\frac{{{na * mx}}}{{{nx}}}"
    kv["line4_RHSq"] = f"\\frac{{{gap}}}{{{gap}}}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv



def div_add_dict():
    # (x / nx) + mx = na
    nx = random.randint(2, 10)
    xval = nx * random.randint(2, 10)
    mx = random.randint(1, 10)
    na = int(xval / nx) + mx

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x}}{{{nx}}} + {mx}"
    kv["line2_LHS"] = f"\\frac{{x}}{{{nx}}} + {mx} - {mx}"
    kv["line2_LHSq"] = f"\\frac{{x}}{{{nx}}} + {mx} - {gap}"
    kv["line3_LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["line4_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{nx}"
    kv["line4_LHSq"] = f"\\frac{{x}}{{{nx}}} \\times{gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} - {mx}"
    kv["line2_RHSq"] = f"{na} - {gap}"
    kv["line3_RHS"] = f"{na - mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na - mx} \\times{nx}"
    kv["line4_RHSq"] = f"{gap} \\times{gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def div_sub_dict():
    # (x / nx) - mx = na
    nx = random.randint(2, 10)
    xval = nx * random.randint(2, 10)
    mx = random.randint(1, 10)
    na = int(xval / nx) - mx

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x}}{{{nx}}} - {mx}"
    kv["line2_LHS"] = f"\\frac{{x}}{{{nx}}} - {mx} + {mx}"
    kv["line2_LHSq"] = f"\\frac{{x}}{{{nx}}} - {mx} + {gap}"
    kv["line3_LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["line4_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{nx}"
    kv["line4_LHSq"] = f"\\frac{{x}}{{{nx}}} \\times{gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na} + {mx}"
    kv["line2_RHSq"] = f"{na} + {gap}"
    kv["line3_RHS"] = f"{na + mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na + mx} \\times{nx}"
    kv["line4_RHSq"] = f"{gap} \\times{gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def div_times_dict():
    # (x / nx) * mx = na
    nx = random.randint(2, 10)
    xval = nx * random.randint(2, 10)
    mx = random.randint(2, 10)
    na = int((xval / nx) * mx)

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{mx}"
    kv["line2_LHS"] = f"\\frac{{\\frac{{x}}{{{nx}}} \\times{mx}}}{{{mx}}}"
    kv["line2_LHSq"] = f"\\frac{{\\frac{{x}}{{{nx}}} \\times{mx}}}{{{gap}}}"
    kv["line3_LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["line4_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{nx}"
    kv["line4_LHSq"] = f"\\frac{{x}}{{{nx}}} \\times{gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"\\frac{{{na}}}{{{mx}}}"
    kv["line2_RHSq"] = f"\\frac{{{na}}}{{{gap}}}"
    kv["line3_RHS"] = f"{int(na / mx)}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{int(na / mx)}\\times{nx}"
    kv["line4_RHSq"] = f"{int(na / mx)}\\times{gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv


def div_div_dict():
    # (x / nx) / mx = na
    nx = random.randint(2, 5)
    mx = random.randint(2, 6)
    na = random.randint(2, 5)
    xval = na * nx * mx

    kv = dict()
    kv["line1_LHS"] = f"\\frac{{\\frac{{x}}{{{nx}}}}}{{{mx}}}"
    kv["line2_LHS"] = f"\\frac{{\\frac{{x}}{{{nx}}}}}{{{mx}}} \\times {mx}"
    kv["line2_LHSq"] = f"\\frac{{\\frac{{x}}{{{nx}}}}}{{{mx}}} \\times {gap}"
    kv["line3_LHS"] = f"\\frac{{x}}{{{nx}}}"
    kv["line4_LHS"] = f"\\frac{{x}}{{{nx}}} \\times{nx}"
    kv["line4_LHSq"] = f"\\frac{{x}}{{{nx}}} \\times{gap}"
    kv["line5_LHS"] = f"x"

    kv["line1_RHS"] = f"{na}"
    kv["line2_RHS"] = f"{na}\\times{mx}"
    kv["line2_RHSq"] = f"{na}\\times{gap}"
    kv["line3_RHS"] = f"{na * mx}"
    kv["line3_RHSq"] = f"{gap}"
    kv["line4_RHS"] = f"{na * mx}\\times{nx}"
    kv["line4_RHSq"] = f"{na * mx}\\times{gap}"
    kv["line5_RHS"] = f"{xval}"
    kv["line5_RHSq"] = f"{gap}"
    return kv
