#!/usr/bin/python3
def weight_average(my_list=[]):
    score = sum([w[1] * w[0] for w in my_list])
    weight = (sum([w[1] for w in my_list]) or 1)
    return score / weight
