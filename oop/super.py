class Parent:
    def __init__(self, name) -> None:
        print("This is parent class", name)


class Parent2:
    def __init__(self, name) -> None:
        print("This is parent2 class", name)

class Child(Parent, Parent2):
    def __init__(self, name) -> None:
        # super function is builtin function that return the proxy object that allows you to refer to parent class

        # we use super() function to call the __init__ function of parent class if we want to pass the argument on the 
        # intialization of the object of child class to the parent class as well.
        print("This is CHILD") 

        # while using the super() function we donot need to pass the self, but like below if 
        # we are using the direct Parent class name and call it's __init__ function we need to pass the self as well
        super().__init__(name)
        

        # * IMPORTANT 
        # if we are using the super() function in multiple inheritence, we will see that child class will only call the 
        # first parent class constructor and not the consutructor of second parent class 
        # to resolve this, we need to manually call the init function of each inherited class 
        Parent.__init__(self,name)
        Parent2.__init__(self,name)
        
        Parent.__init__(self,"Max")
        Parent2.__init__(self,"TOM")



ch = Child("Khan")
# method resolution order 
# this is the method in which order that methods are calling inside child class 
# RULES: method inside sub class will be called first, after that method in base class will be called
# every class is finally inherited from the python object class, so that's why we see "class object" in results of __mro__
# print(Child.__mro__)