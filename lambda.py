'''
Single statement, without named function in python is called lambda function, 
and it is also called as the anonymous function in other programming languages. 

For comprehensive explanation, read python-advance.doc file at github.
'''
sum = lambda a,b: a+b
print(sum(80,90))
print(sum(12,20))

even = lambda a: a%2==0
print(even(5))
print(even(90))



# pass keyword does not work in lambda function so we use elipses
mod = lambda x : x if(x >= 0) else ...
 
print(mod(-1))

a = lambda x: len(x) if (isinstance(x,str)) else None 
a(5)

# https://www.geeksforgeeks.org/lambda-with-if-but-without-else-in-python/





