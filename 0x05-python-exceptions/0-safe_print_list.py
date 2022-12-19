#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    while (x):
        try:
            print("{}".format(my_list[count]), end="")
            count += 1
        except IndexError:
            return
        x -= 1
    print("")
    return (count)
