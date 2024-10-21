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
    # bc = nx + na + nb
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx + na
    bc = bb + nb

    kv = dict()
    kv["stepAB"] = f"+{na}"
    kv["stepABrev"] = f"-{na}"
    kv["stepBC"] = f"+{nb}"
    kv["stepBCrev"] = f"-{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x+{na}"
    kv["boxC"] = f"x+{na + nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
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

    kv = dict()
    kv["stepAB"] = f"+{na}"
    kv["stepABrev"] = f"-{na}"
    kv["stepBC"] = f"-{nb}"
    kv["stepBCrev"] = f"+{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x+{na}"
    if na - nb > 0:
        kv["boxC"] = f"x+{na - nb}"
    else:
        kv["boxC"] = f"x-{nb - na}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def add_times_dict():
    # bc = nx * na * nb
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx + na
    bc = bb * nb

    kv = dict()
    kv["stepAB"] = f"+{na}"
    kv["stepABrev"] = f"-{na}"
    kv["stepBC"] = f"\\times{nb}"
    kv["stepBCrev"] = f"\\div{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x+{na}"
    kv["boxC"] = f"{nb}(x + {na})"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def add_div_dict():
    # bc = (nx + na) / nb
    # nx = (bc * nb) - na
    bc = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = bc * nb
    if bb > 10:
        na = random.randint(1, 10)
    else:
        na = random.randint(1, bb)
    nx = bb - na

    kv = dict()
    kv["stepAB"] = f"+{na}"
    kv["stepABrev"] = f"-{na}"
    kv["stepBC"] = f"\\div{nb}"
    kv["stepBCrev"] = f"\\times{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x+{na}"
    kv["boxC"] = f"\\frac{{(x+{na})}}{{{nb}}}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def sub_add_dict():
    # bc = nx - na + nb
    na = random.randint(1, 10)
    nx = na + random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx - na
    bc = bb + nb

    kv = dict()
    kv["stepAB"] = f"-{na}"
    kv["stepABrev"] = f"+{na}"
    kv["stepBC"] = f"-{nb}"
    kv["stepBCrev"] = f"+{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x-{na}"
    kv["boxC"] = f"x-{na + nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def sub_sub_dict():
    # bc = nx - na - nb
    # nx = bc + nb + na
    bc = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = bc + nb
    nx = bb + na

    kv = dict()
    kv["stepAB"] = f"-{na}"
    kv["stepABrev"] = f"+{na}"
    kv["stepBC"] = f"-{nb}"
    kv["stepBCrev"] = f"+{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x-{na}"
    kv["boxC"] = f"x-{na + nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def sub_times_dict():
    # bc = (nx - na) * nb
    # nx = (bc + nb) * na
    na = random.randint(1, 10)
    nx = na + random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx - na
    bc = bb * nb

    kv = dict()
    kv["stepAB"] = f"-{na}"
    kv["stepABrev"] = f"+{na}"
    kv["stepBC"] = f"\\times{nb}"
    kv["stepBCrev"] = f"\\div{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x-{na}"
    kv["boxC"] = f"{nb}(x-{na})"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def sub_div_dict():
    # bc = nx - na / nb
    # nx = (bc + nb) * na
    bc = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = bc * nb
    nx = bb + na

    kv = dict()
    kv["stepAB"] = f"-{na}"
    kv["stepABrev"] = f"+{na}"
    kv["stepBC"] = f"\\div{nb}"
    kv["stepBCrev"] = f"\\times{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"x-{na}"
    kv["boxC"] = f"\\frac{{(x-{na})}}{{{nb}}}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def times_add_dict():
    # bc = nx * na + nb
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = nx * na
    bc = nx * na + nb

    kv = dict()
    kv["stepAB"] = f"\\times{na}"
    kv["stepABrev"] = f"\\div{na}"
    kv["stepBC"] = f"+{nb}"
    kv["stepBCrev"] = f"-{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"{na}x"
    kv["boxC"] = f"{na}x + {nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def times_sub_dict():
    # bc = nx * na - nb
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    bb = nx * na
    if bb > 10:
        nb = random.randint(2, 10)
    else:
        nb = random.randint(2, bb)
    bc = bb - nb

    kv = dict()
    kv["stepAB"] = f"\\times{na}"
    kv["stepABrev"] = f"\\div{na}"
    kv["stepBC"] = f"-{nb}"
    kv["stepBCrev"] = f"+{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"{na}x"
    kv["boxC"] = f"{na}x - {nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def times_times_dict():
    # bc = nx * na * nb
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = nx * na
    bc = nx * na * nb

    kv = dict()
    kv["stepAB"] = f"\\times{na}"
    kv["stepABrev"] = f"\\div{na}"
    kv["stepBC"] = f"\\times{nb}"
    kv["stepBCrev"] = f"\\div{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"{na}x"
    kv["boxC"] = f"{na * nb}x"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def times_div_dict():
    # bc = nx * na / nb
    nb = random.randint(2, 3)
    na = nb * random.randint(2, 4)
    nx = random.randint(2, 10)
    bb = nx * na
    bc = int(bb / nb)

    kv = dict()
    kv["stepAB"] = f"\\times{na}"
    kv["stepABrev"] = f"\\div{na}"
    kv["stepBC"] = f"\\div{nb}"
    kv["stepBCrev"] = f"\\times{nb}"

    kv["boxA"] = f"x"
    kv["boxB"] = f"{na}x"
    kv["boxC"] = f"{int(na / nb)}x"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def div_add_dict():
    # bc = (nx / na) + nb
    # nx = (bc - nb) * na
    na = random.randint(2, 10)
    nx = na * random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = int(nx / na)
    bc = bb + nb

    kv = dict()
    kv["stepAB"] = f"\\div{na}"
    kv["stepABrev"] = f"\\times{na}"
    kv["stepBC"] = f"+{nb}"
    kv["stepBCrev"] = f"-{nb}"
    kv["boxA"] = f"x"
    kv["boxB"] = f"\\frac{{x}}{{{na}}}"
    kv["boxC"] = f"\\frac{{x}}{{{na}}} + {nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def div_sub_dict():
    # bc = (nx / na) - nb
    # nx = (bc + nb) * na
    bc = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = bc + nb
    nx = bb * na

    kv = dict()
    kv["stepAB"] = f"\\div{na}"
    kv["stepABrev"] = f"\\times{na}"
    kv["stepBC"] = f"-{nb}"
    kv["stepBCrev"] = f"+{nb}"
    kv["boxA"] = f"x"
    kv["boxB"] = f"\\frac{{x}}{{{na}}}"
    kv["boxC"] = f"\\frac{{x}}{{{na}}} - {nb}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def div_times_dict():
    # bc = (nx / na) * nb
    na = random.randint(2, 10)
    nx = na * random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = int(nx / na)
    bc = bb * nb

    kv = dict()
    kv["stepAB"] = f"\\div{na}"
    kv["stepABrev"] = f"\\times{na}"
    kv["stepBC"] = f"\\div{nb}"
    kv["stepBCrev"] = f"\\times{nb}"
    kv["boxA"] = f"x"
    kv["boxB"] = f"\\frac{{x}}{{{na}}}"
    kv["boxC"] = f"\\frac{{x}}{{{na * nb}}}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv


def div_div_dict():
    # bc = (nx / na) / nb
    # escape {} in f strings by doubling them up {{}}
    bc = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = bc * nb
    nx = bb * na

    kv = dict()
    kv["stepAB"] = f"\\div{na}"
    kv["stepABrev"] = f"\\times{na}"
    kv["stepBC"] = f"\\div{nb}"
    kv["stepBCrev"] = f"\\times{nb}"
    kv["boxA"] = f"x"
    kv["boxB"] = f"\\frac{{x}}{{{na}}}"
    kv["boxC"] = f"\\frac{{x}}{{{na * nb}}}"
    kv["boxCrev"] = f"{bc}"
    kv["boxBrev"] = f"{bb}"
    kv["boxArev"] = f"{nx}"
    return kv
