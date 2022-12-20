#!/usr/bin/python3
# 102-square.py
"""setter and getter option creation"""


class Square:
    """Represents a square
    Attributes:
        __size (int): len of side of a square
    """

    def __init__(self, size=0):
        """defining a square class
        Args:
            size(int): len of side of square
        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """gets the size of square
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set as the value to params
        Args:
            value (int): len of a square
        returns:
            None
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Calculates the area of a square and returns result
        Args:
            value (int): size of squares
        """
        return (self.__size) ** 2

    def __lt__(self, other):
        """Compare if square is less than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
