#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
            def area(self):
                return self.__size ** 2
            @property
            def size(self):
                return self.__size
            @size.setter
            def size(self, value):
                if not isinstance(value, int):
                    print("size must be an integer", end="")
                    raise TypeError
                elif value < 0:
                    print("size must be >= 0", end="")
                    raise ValueError
                else:
                    self.__size = value
