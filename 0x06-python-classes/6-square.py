#!/usr/bin/python3
class Square:
      def __init__(self, size=0, position=(0, 0)):
          if not isinstance(size, int):
              raise TypeError("size must be an integer")
          elif size < 0:
              raise ValueError("size must be >= 0")
          else:
              self.__size = size
              if type(position) is not tuple:
                  raise TypeError("position must be a tuple of 2 positive integers")
              elif len(position) != 2:
                  raise TypeError("position must be a tuple of 2 positive integers")
              elif not isinstance(position[0], int):
                  raise TypeError("position must be a tuple of 2 positive integers")
              elif not isinstance(position[1], int):
                  raise TypeError("position must be a tuple of 2 positive integers")
              elif position[0] < 0 or position[1] < 0:
                  raise TypeError("position must be a tuple of 2 positive integers")
              else:
                  self.__position = position
                  def area(self):
                      return self.__size ** 2
                   @property
                   def size(self):
                       return self.__size
                   @size.setter
                   def size(self, value):
                       self.__size = value
                       @property
                       def position(self):
                           return self.__position
                       @position.setter
                       def position(self, value):
                           self.__position = value

                           def my_print(self):
                               if self.__size == 0:
                                   print()
                               else:
                                   for emptyrow in range(0, self.__position[1]):
                                       print()
                                       for row in range(0, self.__size):
                                           for space in range(0, self.__position[0]):
                                               print(" ", end="")
                                               for octothorpe in range(0, self.__size):
                                                   print("#", end="")
                                                   print()
