class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return ((22/7)*self.radius**2)
    
    def perimeter(self):
        return ((22/7)*self.radius*2)
    
c1 = circle(21)
print(c1.area())
print(c1.perimeter())