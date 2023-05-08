

class CircleShape():
    ''' 
     A class to represent a circle'''
    def __init__(self,radius):
        self.my_radius = radius

    def area(self):
        return self.my_radius**2*3.14
    
    def perimeter(self):
        return 2*self.my_radius*3.14
    
Newcircle = CircleShape(7)
print(Newcircle.area())
print(Newcircle.perimeter())
