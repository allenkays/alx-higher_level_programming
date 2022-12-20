#!/usr/bin/python3
# 6-square.py
"""setter and getter option creation"""


class Square:
    """Represents a square
    Attributes:
        __size (int): len of side of a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """defining a square class
        Args:
            size(int): len of side of square
        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current position of the square.
        Args:
            position coordinates
        Returns:
            position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of a square and returns result
        Args:
            value (int): size of squares
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints the square with '#'
        returns: none
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
