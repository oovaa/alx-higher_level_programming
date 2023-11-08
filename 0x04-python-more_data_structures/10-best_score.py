#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    scores = list(a_dictionary.values())
    names = list(a_dictionary.keys())
    return names[scores.index(max(scores))]
