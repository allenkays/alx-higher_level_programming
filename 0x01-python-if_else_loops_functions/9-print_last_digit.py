#!/usr/bin/python3
'''
print_last_digit - prints last digit of a number
@number: number to print last digit for
'''


def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return (abs(number) % 10)
