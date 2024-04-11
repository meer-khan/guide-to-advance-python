'''
Generators: By using the yield keyword instead of return, we make the function as Generator, 
in other words, if we used yield keyword in the function, that function will be called Generator.  
Important: we use the next() object to call that particular generator again and again. 

For comprehensive explanation, read python-advance.doc file at github.

'''
import os,sys

def list_generator(l1): 
    for i in l1: 
        yield i


l1=[1,2,3,4]
a = list_generator(l1)
print(next(a))
print(next(a))
print(next(a))

def yeildTest (a):
    return a+8

'''
Yield keyword can alos be used with the return statement in the same generator function, 
return statement will be executed when yield will return all it's data 
'''
def test(l1):
    for i in l1: 
        print(i)
        yield i
    print("print line after the yield keyword")
    # return True 

a = test(l1)
print(type(a))
print(sys.getsizeof(a))

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


a = 5 
b = "hello"
c = (1,2,3)
d=[1,2,3]

print("id of d: ", id(d))
d.append(5)
print("id of d: ", id(d))
