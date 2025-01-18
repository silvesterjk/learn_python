# @property decorator is used to define a property. It allows you to access a method like an attribute.
# Benefits of using the @property decorator: It allows you to access a method like an attribute. It also allows you to define a method that can be accessed like an attribute.
# Gives you the ability to define a method that can be accessed like an attribute. It also allows you to define a method that can be accessed like an attribute.
# Getter, setter, and deleter methods can be defined using the @property decorator.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

Rectangle1 = Rectangle(10, 20)
print(Rectangle1.length) # Accessing the length attribute of the Rectangle1 object
print(Rectangle1.width) # Accessing the width attribute of the Rectangle1 object

"""

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if new_width < 0:
            raise ValueError('Width must be greater than 0')
        elif new_width > 0:
            self._width = new_width
        else:
            raise ValueError('Width must be greater than 0')
    
    @width.deleter
    def width(self):
        del self._width
        print('Width has been deleted')

Rectangle1 = Rectangle(10, 20)
print(Rectangle1.length) # Accessing the length attribute of the Rectangle1 object
print(Rectangle1.width) # Accessing the width attribute of the Rectangle1 object