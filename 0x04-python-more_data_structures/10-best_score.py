#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    maxval = 0
    maxkey = None
    for k, v in a_dictionary.items():
        if v > maxval:
            maxval = v
            maxkey = k
    return maxkey
