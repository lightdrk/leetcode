class Rectangle:
  def __init__(self, width, height):
    self.__width = width
    self.__height = height
  def area(self):
    return self.__width * self.__height

a = Rectangle(1,2)
print(a.__width)
