#!/usr/bin/python3
def best_score(a_dictionary):
        if a_dictionary is None:
                return None
        best = 0
        best_key = None
        for key, val in a_dictionary.items():
                if val > best:
                        best = val
                        best_key = key
        return best_key
