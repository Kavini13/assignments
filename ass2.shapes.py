#circle
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

#Rectangle
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
#rhombus
from math import sqrt , pow
def rhombusArea(diagonal1 , diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return ("The area of rhombus with diagonals", diagonal1, "and", diagonal2, "is", area)
def rhombusPeri(diagonal1 , diagonal2):
    perimeter = 2 * sqrt(pow(diagonal1 , 2) + pow(diagonal2 , 2))
    return ("The perimeter of rhombus with diagonals", diagonal1, "and", diagonal2, "is", perimeter)

if __name__ == '__main__':
    diagonal1 = int(input(" enter the value of diagonal1:"))
    diagonal2 = int(input(" enter the value of diagonal2:"))
    print(rhombusArea(diagonal1 , diagonal2))
    print(rhombusPeri(diagonal1,diagonal2))

# Triangle
class Triangle:
    
    def findPerimeter(self, num1, num2, num3):
        return num1 + num2 + num3

    def findArea(self, num1, num2, num3):
        perimeter = (num1 + num2 + num3)
        area = perimeter / 2
        return (area * (area - num1) * (area - num2) * (area - num3)) ** 0.5


num1 = float(input("Enter the first side of triangle:"))
num2 = float(input("Enter the second side of triangle:"))
num3 = float(input("Enter the third side of triangle:"))

newTriangle = Triangle()

print("The perimeter of triangle is: {0:2f}".format(newTriangle.findPerimeter(num1, num2, num3)))
print("The area of triangle is: {0:2f}".format(newTriangle.findArea(num1, num2, num3)))
   

