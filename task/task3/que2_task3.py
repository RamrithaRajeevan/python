#create class called Rectangle with private attributes for width & height.Provide getter & setter method to access & modify these attribute . Iclude method to calculate area of rectangle.
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

rect = Rectangle(4, 5)

print(f"Width: {rect.width}")  
print(f"Height: {rect.height}") 

rect.width = 10
rect.height = 20

print(f"Modified Width: {rect.width}")  
print(f"Modified Height: {rect.height}") 

print(f"Area: {rect.area()}") 


