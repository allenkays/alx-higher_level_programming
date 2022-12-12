#!/usr/bin/python3

def weight_average(my_list=[]):
    """Return weighted average of int in a list of tuples."""
    if my_list != list(my_list) or len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for x in my_list:
        average += (x[0] * x[1])
        size += x[1]
    return (average / size)
