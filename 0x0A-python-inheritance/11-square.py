#!/usr/bin/python3
# 11-square.py
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Derived class"""

    def __init__(self, size):
        """instancesiate a new square"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """represents a description of a square"""
        return ("[" + str(self.__class__.__name__) + "] "
                + str(self.__size) + "/" + str(self.__size))
