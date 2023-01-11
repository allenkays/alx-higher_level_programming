#!/usr/bin/python3
# 100-my_int.py
"""Derived class MyInt from int."""


class MyInt(int):
    """Invert int comparison operators == and !=."""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
