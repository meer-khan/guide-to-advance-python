import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius): 
        self.__radius = radius

    
    def area(self):

        return math.pi * self.__radius ** 2
    
    def __add__(self, circle_object): 
        return Circle(self.__radius + circle_object.__radius)
    
    def __lt__(self, circle_object):
        return self.__radius < circle_object.__radius
    
    
    def __gt__(self, circle_object):
        return self.__radius > circle_object.__radius
    

    def __str__(self):
        print(self.area())
        return "Area of circle is: " + str(self.area())
    

c1 = Circle(5)

c2 = Circle(4)

c3 = c1 + c2

print(c1.get_radius())
print(c2.get_radius())
print(c3.get_radius())

print(c1 > c2)
print(c1 < c2)

# dir function returns the functions associated with the python class objects
print(dir(c1))
print(c3)


a = "PK", 90, 00, 100
print(type(a))
print(a)