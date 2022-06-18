#!/usr/bin/python3
def best_score(a_dictionary):
    if not type(a_dictionary) is dict:
        return None

    if len(a_dictionary) == 0:
        return None

    retval = list(a_dictionary.keys())[0]
    bigval = a_dictionary[retval]
    for k, v in a_dictionary.items():
        if v > bigval:
            bigval = v
            retval = k
    return retval
