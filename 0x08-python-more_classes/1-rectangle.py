#!/usr/bin/python3

"""
Empty class rectangle
"""


class Rectangle:
    """class to define a rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle object
            Args:
                    width (int): width of the rectangle
                    height (int): hight of the rectangle
            Raise:
                    TypeError: if any of the args are not ints
                    ValueError: if any of the args are less than 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """set width of rectangle"""
        return self.__width

    @width.setter
    def width(self):
        """check type and value of width input"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height

    @height.setter
    def height(self):
        """check height type and value input"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
