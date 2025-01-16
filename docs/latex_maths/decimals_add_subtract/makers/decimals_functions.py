"""
Module of functions to return decimals dictionary for LaTeX
"""

import random


def get_dec_dict(nump, numip, numdp):
    if nump is None or nump == 3:
        nump = random.randint(1, 2)
    match nump:
        case 1:
            return add_dict(numip, numdp)
        case 2:
            return sub_dict(numip, numdp)


def add_dict(numip, numdp):
    # na + nb = nc
    # Generate a random decimal number between 0.00001 and 9999
    na = random.uniform(10**-numdp, (10**numip) - 0.1)
    nb = random.uniform(10**-numdp, (10**numip) - 0.1 - na)
    # Format the result to 0 to 5 decimal places
    format_string = "{:." + str(numdp) + "f}"
    na = format_string.format(na)
    nb = format_string.format(nb)
    nc = float(na) + float(nb)
    nc = format_string.format(nc)
    kv = dict()
    kv["num1"] = f"{na}"
    kv["num2"] = f"{nb}"
    kv["process"] = "+"
    kv["answer"] = f"{nc}"
    kv["numip"] = f"{str(numip)}"
    kv["numdp"] = f"{str(numdp)}"
    return kv


def sub_dict(numip, numdp):
    # na + nb = nc
    # Generate a random decimal number between 0.01 and 100
    nc = random.uniform(10**-numdp, (10**numip) - 0.1)
    nb = random.uniform(10**-numdp, (10**numip) - 0.1 - nc)
    # Format the result to 0 to 5 decimal places
    format_string = "{:." + str(numdp) + "f}"
    nc = format_string.format(nc)
    nb = format_string.format(nb)
    na = float(nc) + float(nb)
    na = format_string.format(na)
    #
    kv = dict()
    kv["num1"] = f"{na}"
    kv["num2"] = f"{nb}"
    kv["process"] = "-"
    kv["answer"] = f"{nc}"
    kv["numip"] = f"{str(numip)}"
    kv["numdp"] = f"{str(numdp)}"
    return kv

