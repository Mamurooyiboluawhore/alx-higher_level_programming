#!/usr/bin/python3
""" a script that writes an empty class called square"""


class Square:
    """ a class with a private instance attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
