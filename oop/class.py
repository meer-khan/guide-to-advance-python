from shape import Shape

class Car:

    # This is exactly not the constructor but very close to the constructor, we call it a constructor because it is the first method that is called when 
    # we create the object of a class. (Explre difference between the constructor and __init__ method of python class)
    # using self is convention, we can use any variable here, as we know self is called automatically by the "object" class or we can say by python 
    # and it is a requirement that we need to give one argument in __init__ method. 
    # We cannot initilize 2 __init__ methods in python.
    # we can provide default value of arugment as well as we can provide *args (multiple parameters) and **kwargs (keyword arguments(it will be get as a dictionary)).
    # we can also provide a default value by just writing 
    # self.age = 10
    # into body of __init__ function and not in argument 

    # * Encapsulation: 
    # Java and C++ has public private method to encapsulate means to hide the information from the user to change it, let's say e.g.
    # all the class variables can be easily accessed and modified by the instance, and we donot want that, 
    # to encapsulate this information, we make getters and setters, and make all class variables private (majority of them)
    # by making getters and setter funtions we can get control over what variables can be accessed through getters and what can be modified 
    # and in the modification, user can give string value to some variable that only operates on string, so we can also handle such information gracefully through setters
        # * Private Member variables 
        # Only accessible in the class, not outside the class
        # To make variables private we donot have any function public, private, protected etc just lke JAVA and C++, but we have 2 methods to make a variable private 
        # 1. using single _ with variable name, it's just a convention to make a variable private but it does not actually
        # 2. using double __ with variable name makes it actually private
        # to change the value of private variables we use, setter functions

        # Similarly we can also create private methods, that are only accessible in same class and not outside the class
    def __init__(self,speed,color, _b=10,__c=30) -> None:
        print("__INIT__") 
        self.speed = speed
        self.color = color
        self.model = 2023
        self._b = _b
        self.__c = __c
        print(speed, color)

    def set_c(self, __c):
        self.__c = __c

    def get_c(self):
        return self.__c
    
class Polygon:
    print("Polygon")

    __width = None
    __height = None 
    def set_values(self,width,height):
        self.__width = width
        self.__height = height
    
    def get_width (self):
        return self.__width
    def get_height (self):
        return self.__height

class Rectangle(Polygon, Shape):
    print("Rectangle")

    def area(self):
        return self.get_width() * self.get_height()
    

class Triangle(Polygon, Shape):
    print("Triangle")
    def area(self):
        return (self.get_width() * self.get_height()) / 2


 

ford = Car(200,'red')
honda = Car(200,'green')
audi = Car(200,'blue')

# ford.speed = 200
# honda.speed = 200
# audi.speed = 200

# ford.color = 'red'
# honda.color = 'blue'
# audi.color = 'green'

print(audi.speed, audi.color)
print(audi)
print(audi.model)
# print(audi._b)
# print(audi.__c)
audi.set_c(100)
print(audi.get_c())

print("**********************************")
rect = Rectangle()
tri = Triangle()

rect.set_values(50,20)
print(rect.area())


tri.set_color("Black")
print(tri.get_color())



