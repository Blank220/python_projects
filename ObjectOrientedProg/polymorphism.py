from abc import abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
         
class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side * self.side
         

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5
         
class Pizza(Circle):
    def __init__(self,radius,topping):
        super().__init__(radius)
        self.topping = topping
        

shapes = [Circle(5), Square(8), Triangle(6,7), Pizza(9,'Hotdog')]

for shape in shapes:
    print(f"The area is {shape.area()}cm²")