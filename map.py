def find_even_odd(num): 
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list(map(find_even_odd,l1)))

# def getLength(x):
#     return(len(x))

# iter_Dict = {"Python":"Hello", "CSharp":"BHAI", "Java":"BEHEN"}
# print(iter_Dict)


# # Calling map() function on a dictionary
# map_result =  map(getLength, iter_Dict)
# print(list(map_result))
