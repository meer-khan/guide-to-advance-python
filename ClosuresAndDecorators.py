'''
Closure: Closure in Python is an inner function object, a function that behaves like an object, 
that remembers and has access to variables in the local scope 
(inner function have all the access of the variables and parameters of outer function) 
in which it was created even after the outer function has finished executing.

Simple defintion: Fuction in a function is called closures in python 
'''

def deco(func):
    print("Hello Saturn!")
    x = 10
    func(x)
    return 7

# @deco()
def myfunc(x):
    z = x+30
    print(z)
    print("Hello Earth!")

# --------------------------------------------------------------------------------------------------------------
# or you can use the closure property as well with decorators

def deco(func):
    print("Hello Mars!")
    x = 10
    def innerFunc():
        func(x)

    return innerFunc

'''
As you can see above we call the inner function of deco() function in it's return statement because 
inner function cannot be called out of the scope of the outer functions and they have access of all global as well as 
outer function's parameters 
'''
'''
A decorator is a design pattern in Python that allows a user to add new functionality to an 
existing object without modifying its structure. Decorators are usually called before the 
definition of a function you want to decorate.
'''
@deco 
def myfunc(x=10):
    z = x+30
    print(z)
    print("Hello Earth!")
    return "End of Execution"


call = deco(myfunc)
# call()


#  Decorators Chainning: 

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print("Last output",num())

# it is same as decor1(decor(num))