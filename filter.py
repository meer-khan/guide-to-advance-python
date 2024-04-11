
print("---------Filter function without boolean value return--------------")
def find_even_odd(num): 
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list(filter(find_even_odd,l1)))

# The above code will work exactly same as the map function because we are not using 
# the boolean data types(True, False) in the return statement. 


print("---------Filter function with boolean value return--------------")
def find_even_odd(num): 
    if num%2 == 0:
        return True
    else:
        return False

l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list(filter(find_even_odd,l1)))