# Python doesnot have builtin functionality of creating the abstract classes but we can do it using the "abc" module 
# we cannot create objects of abstract classes, rather we need to create an object of child class in which 
# methods of abstracted classes are overriddent

from abc import ABC, abstractmethod
# ABC stands for Abstract base classes

class Shape(ABC): 
    '''
    Class becomes abstract, when we use @abstractmethod decorator for atleast one method in the class 
    if any class is inherited by the ABC class and doesnot have any method that use decorator of @abstractmethod 
    then class will not be the abstract class

    Abstract classes acts as a template for the classes that inherits this class
    
    '''
    @abstractmethod
    def parameter(): pass

    @abstractmethod
    def area(): pass


class Square(Shape):
    '''
    Any class inherited the abstract class should always override the abstract methods of the parent class 
    other wise we cannot use the child class
    python will throw error if we try to instanciate the object of Square class
    '''
    def __init__(self, side) -> None:
        super().__init__()
        self.__side = side 

    
    def area(self): 
        return self.__side * self.__side
    
    def parameter(self):
        return 4*self.__side


# Below line will throw error, because we cannot instanciate the abstract classes, we can only inherit it 
# TypeError: Can't instantiate abstract class Shape with abstract methods area, parameter
# shape = Shape()


square = Square(5)
print(square.area())
print(square.parameter())


