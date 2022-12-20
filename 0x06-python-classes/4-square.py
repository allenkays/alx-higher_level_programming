#!/usr/bin/python3
# 4-square.py
"""setter and getter option creation"""


class Square:

    def __init__(self, size=0):
        """defining a square class"""
        self.__size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setas the value to params"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Calculates the area of a square and returns result"""
        return (self.__size ** 2)
