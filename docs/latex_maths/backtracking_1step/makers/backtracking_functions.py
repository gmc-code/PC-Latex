"""
Module of functions to return diagram dictionary for LaTeX
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
    # bb = nx + na
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    bb = nx + na
    mod_dict = dict()
    mod_dict["stepAB"] = f"+{na}"
    mod_dict["stepABrev"] = f"-{na}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x+{na}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def sub_dict():
    # bb = nx - na
    na = random.randint(1, 10)
    nx = na + random.randint(1, 10)
    bb = nx - na
    mod_dict = dict()
    mod_dict["stepAB"] = f"-{na}"
    mod_dict["stepABrev"] = f"+{na}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x-{na}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def times_dict():
    # bb = nx * na
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    bb = nx * na
    mod_dict = dict()
    mod_dict["stepAB"] = f"\\times{na}"
    mod_dict["stepABrev"] = f"\\div{na}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"{na}x"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def div_dict():
    #  bb = nx / na; nx = na * bb
    # escape {} in f strings by doubling them up {{}}
    na = random.randint(2, 10)
    nx = na * random.randint(2, 10)
    bb = int(nx / na)
    mod_dict = dict()
    mod_dict["stepAB"] = f"\\div{na}"
    mod_dict["stepABrev"] = f"\\times{na}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"\\frac{{x}}{{{na}}}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict



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

    mod_dict = dict()
    mod_dict["stepAB"] = f"+{na}"
    mod_dict["stepABrev"] = f"-{na}"
    mod_dict["stepBC"] = f"+{nb}"
    mod_dict["stepBCrev"] = f"-{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x+{na}"
    mod_dict["boxC"] = f"x+{na + nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


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

    mod_dict = dict()
    mod_dict["stepAB"] = f"+{na}"
    mod_dict["stepABrev"] = f"-{na}"
    mod_dict["stepBC"] = f"-{nb}"
    mod_dict["stepBCrev"] = f"+{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x+{na}"
    if na - nb > 0:
        mod_dict["boxC"] = f"x+{na - nb}"
    else:
        mod_dict["boxC"] = f"x-{nb - na}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def add_times_dict():
    # bc = nx * na * nb
    nx = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx + na
    bc = bb * nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"+{na}"
    mod_dict["stepABrev"] = f"-{na}"
    mod_dict["stepBC"] = f"\\times{nb}"
    mod_dict["stepBCrev"] = f"\\div{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x+{na}"
    mod_dict["boxC"] = f"{nb}(x + {na})"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


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

    mod_dict = dict()
    mod_dict["stepAB"] = f"+{na}"
    mod_dict["stepABrev"] = f"-{na}"
    mod_dict["stepBC"] = f"\\div{nb}"
    mod_dict["stepBCrev"] = f"\\times{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x+{na}"
    mod_dict["boxC"] = f"\\frac{{(x+{na})}}{{{nb}}}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def sub_add_dict():
    # bc = nx - na + nb
    na = random.randint(1, 10)
    nx = na + random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx - na
    bc = bb + nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"-{na}"
    mod_dict["stepABrev"] = f"+{na}"
    mod_dict["stepBC"] = f"-{nb}"
    mod_dict["stepBCrev"] = f"+{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x-{na}"
    mod_dict["boxC"] = f"x-{na + nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def sub_sub_dict():
    # bc = nx - na - nb
    # nx = bc + nb + na
    bc = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = bc + nb
    nx = bb + na

    mod_dict = dict()
    mod_dict["stepAB"] = f"-{na}"
    mod_dict["stepABrev"] = f"+{na}"
    mod_dict["stepBC"] = f"-{nb}"
    mod_dict["stepBCrev"] = f"+{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x-{na}"
    mod_dict["boxC"] = f"x-{na + nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def sub_times_dict():
    # bc = (nx - na) * nb
    # nx = (bc + nb) * na
    na = random.randint(1, 10)
    nx = na + random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = nx - na
    bc = bb * nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"-{na}"
    mod_dict["stepABrev"] = f"+{na}"
    mod_dict["stepBC"] = f"\\times{nb}"
    mod_dict["stepBCrev"] = f"\\div{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x-{na}"
    mod_dict["boxC"] = f"{nb}(x-{na})"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def sub_div_dict():
    # bc = nx - na / nb
    # nx = (bc + nb) * na
    bc = random.randint(1, 10)
    na = random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = bc * nb
    nx = bb + na

    mod_dict = dict()
    mod_dict["stepAB"] = f"-{na}"
    mod_dict["stepABrev"] = f"+{na}"
    mod_dict["stepBC"] = f"\\div{nb}"
    mod_dict["stepBCrev"] = f"\\times{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"x-{na}"
    mod_dict["boxC"] = f"\\frac{{(x-{na})}}{{{nb}}}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def times_add_dict():
    # bc = nx * na + nb
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = nx * na
    bc = nx * na + nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\times{na}"
    mod_dict["stepABrev"] = f"\\div{na}"
    mod_dict["stepBC"] = f"+{nb}"
    mod_dict["stepBCrev"] = f"-{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"{na}x"
    mod_dict["boxC"] = f"{na}x + {nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


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

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\times{na}"
    mod_dict["stepABrev"] = f"\\div{na}"
    mod_dict["stepBC"] = f"-{nb}"
    mod_dict["stepBCrev"] = f"+{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"{na}x"
    mod_dict["boxC"] = f"{na}x - {nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def times_times_dict():
    # bc = nx * na * nb
    nx = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = nx * na
    bc = nx * na * nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\times{na}"
    mod_dict["stepABrev"] = f"\\div{na}"
    mod_dict["stepBC"] = f"\\times{nb}"
    mod_dict["stepBCrev"] = f"\\div{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"{na}x"
    mod_dict["boxC"] = f"{na * nb}x"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def times_div_dict():
    # bc = nx * na / nb
    nb = random.randint(2, 3)
    na = nb * random.randint(2, 4)
    nx = random.randint(2, 10)
    bb = nx * na
    bc = int(bb / nb)

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\times{na}"
    mod_dict["stepABrev"] = f"\\div{na}"
    mod_dict["stepBC"] = f"\\div{nb}"
    mod_dict["stepBCrev"] = f"\\times{nb}"

    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"{na}x"
    mod_dict["boxC"] = f"{int(na / nb)}x"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def div_add_dict():
    # bc = (nx / na) + nb
    # nx = (bc - nb) * na
    na = random.randint(2, 10)
    nx = na * random.randint(1, 10)
    nb = random.randint(1, 10)
    bb = int(nx / na)
    bc = bb + nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\div{na}"
    mod_dict["stepABrev"] = f"\\times{na}"
    mod_dict["stepBC"] = f"+{nb}"
    mod_dict["stepBCrev"] = f"-{nb}"
    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"\\frac{{x}}{{{na}}}"
    mod_dict["boxC"] = f"\\frac{{x}}{{{na}}} + {nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def div_sub_dict():
    # bc = (nx / na) - nb
    # nx = (bc + nb) * na
    bc = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = bc + nb
    nx = bb * na

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\div{na}"
    mod_dict["stepABrev"] = f"\\times{na}"
    mod_dict["stepBC"] = f"-{nb}"
    mod_dict["stepBCrev"] = f"+{nb}"
    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"\\frac{{x}}{{{na}}}"
    mod_dict["boxC"] = f"\\frac{{x}}{{{na}}} - {nb}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def div_times_dict():
    # bc = (nx / na) * nb
    na = random.randint(2, 10)
    nx = na * random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = int(nx / na)
    bc = bb * nb

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\div{na}"
    mod_dict["stepABrev"] = f"\\times{na}"
    mod_dict["stepBC"] = f"\\div{nb}"
    mod_dict["stepBCrev"] = f"\\times{nb}"
    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"\\frac{{x}}{{{na}}}"
    mod_dict["boxC"] = f"\\frac{{x}}{{{na * nb}}}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict


def div_div_dict():
    # bc = (nx / na) / nb
    # escape {} in f strings by doubling them up {{}}
    bc = random.randint(2, 10)
    na = random.randint(2, 10)
    nb = random.randint(2, 10)
    bb = bc * nb
    nx = bb * na

    mod_dict = dict()
    mod_dict["stepAB"] = f"\\div{na}"
    mod_dict["stepABrev"] = f"\\times{na}"
    mod_dict["stepBC"] = f"\\div{nb}"
    mod_dict["stepBCrev"] = f"\\times{nb}"
    mod_dict["boxA"] = f"x"
    mod_dict["boxB"] = f"\\frac{{x}}{{{na}}}"
    mod_dict["boxC"] = f"\\frac{{x}}{{{na * nb}}}"
    mod_dict["boxCrev"] = f"{bc}"
    mod_dict["boxBrev"] = f"{bb}"
    mod_dict["boxArev"] = f"{nx}"
    return mod_dict
