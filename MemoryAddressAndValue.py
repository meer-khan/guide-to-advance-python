import ctypes
from re import A

def welcome():
    return "Hello World!"

'''
You can get the memory address of any varible by using the id() function
and then get the value stored on that memory address using the ctypes class which is used to
deal wil thee DLL and shared library files- you can see the functions of ctypes class at line 19 
'''
wel = welcome
print("Memory address of welcome function: ",id(welcome))
del welcome
print(wel())
# we will see that even after deleting the welcome function, we can access it using our copy which is stored in the "wel" variable.
print("Memory address of wel variable which is copy of welcome() function: ",id(wel))
welID = id(wel)
print(id(welID))
print(ctypes.cast(id(wel),ctypes.py_object).value)

a = 10
b = a 

print(id(a))
print(id(b))
b = 7
print(b)
print(id(b))
print(id(a))
b = 19
print(id(b))
print(ctypes.cast(id(a),ctypes.py_object).value)
print(ctypes.cast(id(b),ctypes.py_object).value)
