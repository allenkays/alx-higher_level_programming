#!/usr/bin/python3
# 9-rectangle.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ Instanciate a new rectangle

            Args:
                width(int): width of the rectangle
                height(int): height of the rectangle
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """outputs the dimensions of the rectangle"""
        return ("[" + str(self.__class__.__name__) + "] " +
                str(self.__width) + "/" + str(self.__height))
