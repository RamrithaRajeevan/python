#create base class called shape with method area.create subclasses circle,square &triangle that implement area method.Demonstrate polymorphism bh creating list of different shape objects and iterating throungh it to calculate their areas. 

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=22/7
        return pi*(self.radius**2)
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2   
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
    
shapes=[Circle(4),Square(8),Triangle(4,2),Square(6),Circle(2)]
for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
