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
        self.__size = size
        self.__position = position

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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__size == 0:
            print()
            return
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
