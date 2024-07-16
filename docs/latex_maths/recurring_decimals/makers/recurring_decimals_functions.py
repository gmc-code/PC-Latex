"""
Module of functions to return decimals dictionary for LaTeX
"""
import random


# from fractions import Fraction
# from decimal import Decimal, getcontext


def get_num_denom_pairs_list(shuffle_bool=True):
    """list of possible rec dec fractions (nominator, denomiator)"""
    num_denom_pairs_list = [
        (1, 3),
        (2, 3),
        (1, 6),
        (5, 6),
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
        (1, 9),
        (2, 9),
        (4, 9),
        (5, 9),
        (7, 9),
        (8, 9),
        (1, 11),
        (2, 11),
        (3, 11),
        (4, 11),
        (5, 11),
        (6, 11),
        (7, 11),
        (8, 11),
        (9, 11),
        (10, 11),
    ]
    if shuffle_bool:
        random.shuffle(num_denom_pairs_list)
    return num_denom_pairs_list


def repeating_dec_sol(numerator, denominator):
    """returns rec dec like 2.1(6) with the 6 recurring"""
    negative = False
    if denominator == 0:
        return "Undefined"
    if numerator == 0:
        return "0"
    if numerator * denominator < 0:
        negative = True
    if numerator % denominator == 0:
        return str(numerator / denominator)

    num = abs(numerator)
    den = abs(denominator)

    output = ""
    output += str(num // den)
    output += "."

    quotient_num = []
    while num:
        # In case the remainder is equal to zero, there are no repeating
        # decimals. Therefore, we don't need to add any parenthesis and we can
        # break the while loop and return the output.
        remainder = num % den
        if remainder == 0:
            for i in quotient_num:
                output += str(i[-1])
            break
        num = remainder * 10
        quotient = num // den

        # If the new numerator and quotient are not already in the list, we
        # append them to the list.
        if [num, quotient] not in quotient_num:
            quotient_num.append([num, quotient])
        # If the new numerator and quotient are instead already in the list, we
        # break the execution and we prepare to return the final output.
        # We take track of the index position, in order to add the parenthesis
        # at the output in the right place.
        elif [num, quotient] in quotient_num:
            index = quotient_num.index([num, quotient])
            for i in quotient_num[:index]:
                output += str(i[-1])
            output += "("
            for i in quotient_num[index:]:
                output += str(i[-1])
            output += ")"
            break
    if negative:
        output = "-" + output
    return output


def get_rec_dec_parts(recdec):
    # delete trainligng )
    recdec = recdec[:-1]
    split_string_list = recdec.split("(")
    return split_string_list[0], split_string_list[1]


def rec_dec_dict(numerator, denominator):
    # $$\frac{<<num>>}{<<denom>>} =<<nonrepeating>> \overline {<<repeating>>}$$
    recdec = repeating_dec_sol(numerator, denominator)
    nonrepeating, repeating = get_rec_dec_parts(recdec)
    #
    kv = dict()
    kv["numerator"] = f"{numerator}"
    kv["denominator"] = f"{denominator}"
    kv["nonrepeating"] = f"{nonrepeating}"
    kv["repeating"] = f"{repeating}"
    return kv


# if __name__ == "__main__":
#     print("starting")
#     print(get_num_denom_pairs_list())
#     print("finished")
# print(repeating_dec_sol(452,495), 913/999)

