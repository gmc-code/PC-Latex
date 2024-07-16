"""
Module of functions to return diagram dictionary for LaTeX
"""
import random


def get_lever_dict(num):
    if num is None or num == 4:
        num = random.randint(1, 3)
    match num:
        case 1:
            return first_class_lever_dict()
        case 2:
            return first_class_lever_dict()
        case 3:
            return first_class_lever_dict()




def first_class_lever_dict():
    # 6 cm on screen to represent dist_l + dist_e
    # ma from 1 to 10
    fl = random.randrange(10, 101, 5)
    ma = random.choice([1,1.5,2,2.5,3,4,5,6,8,9,10])
    fe = round(fl/ma,2)
    fulc = 6/(ma + 1)
    fulc_c = round(fulc,2)
    fulc_l = round(fulc - 0.2,2)
    fulc_r = round(fulc + 0.2,2)
    dl = round(fulc * 10,1)
    de = round(60 - (fulc * 10),1)
    # load vector 2.5cm on page; effort vector
    ev = round(-2.5/ma,2)

    kv = dict()
    kv["force_l"] = f"{fl}"
    kv["force_e"] = f"{fe}"
    kv["dist_l"] = f"{dl}"
    kv["dist_e"] = f"{de}"

    kv["ans_force_l"] = f"{fl}"
    kv["ans_force_e"] = f"{fe}"
    kv["ans_dist_l"] = f"{dl}"
    kv["ans_dist_e"] = f"{de}"

    kv["fulc_c"] = f"{fulc_c}"
    kv["fulc_l"] = f"{fulc_l}"
    kv["fulc_r"] = f"{fulc_r}"

    kv["effort_vector"] = f"{ev}"

    return kv