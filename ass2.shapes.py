class CircleShape():

    def __init__(self, radius):
        self.my_radius = radius

    def area(self):
        return self.my_radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.my_radius * 3.14


newCircle = CircleShape(8)
print(newCircle.area())
print(newCircle.perimeter())


class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def rectangle_area(self):
        return self.length * self.breadth

    def rectangle_perimeter(self):
        return 2*self.length + 2*self.breadth


newRectangle = Rectangle(12
10)
print(newRectangle.rectangle_
area())
print(newRectangle.rectangle_perimeter())


class Triangle:
    def __init__(self,):

