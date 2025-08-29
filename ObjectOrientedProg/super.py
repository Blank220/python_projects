class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'It is {self.color} and {'filled' if self.is_filled else 'not filled'}')

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f'It is a circle with an area of {3.14 * self.radius ** 2}cm^2')
        

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f'It is a square with an area of {self.width * self.width}cm^2')

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        super().describe()
        print(f'It is a triangle with an area of {self.width * self.height // 2}cm^2')


circle = Circle(color='green', is_filled=True, radius=12)
square = Square(color='red', is_filled=False, width= 5 )
triangle = Triangle(color='yellow', is_filled=True, width=12, height=9)

print(f'The circle is color {circle.color}')
print(circle.is_filled)
print(f'The radius of the circle is {circle.radius}cm')
print()
circle.describe()
print()
square.describe()
print()
triangle.describe()