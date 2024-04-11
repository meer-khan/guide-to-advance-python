'''
= : works in iterators just to refer the same iterator object to other v
ariable, and if we change either of the variable, we will see the alteration 
in both of the variables. 

Shallow Copy: copy() method works fine on the single dimensional list, 
if we make change in one variable of iterator then it wont reflect back 
on the other variable but it is not a case for the 2D or above dimensional 
lists, So Python came up with Deep copy concept. 

Deep Copy: it is method/function of copy class so we need to import copy first 
in our code to use its copy.deepcopy() method/function, and it works find with 
either single dimensional lists or multiple dimensional lists. 
'''

# First we will look at the "=" function on lists 

list1 = [1,2,3,4]
list2 = list1

list1[1] = 1000
print("List1 by using \"=\": ", list1)
print("List2 by using \"=\": ",list2)

# As we can see in the output that only by changing the 1st index of list1,
# Python changed the list2 as well, this is because of by using the "=" operator 
# list1 and list2 are referencing the same memory addres 


# Now we will talk about the Shallow Copy which can be achieved by using the Python's copy() function 
print("------------------------Shallow Copy----------------------------")
list1 = [1,2,3,4]
list2 = list1.copy()

list1[1] = 1000
print("list1 by using copy() function: ",list1)
print("list2 by using copy() function: ",list2)

# But copy() function wont work on the nested lists, 
# If we make any change in either of the 2 lists, it will be reflect back in both of the lists 
print("------------------------Shallow Copy with nested lists----------------------------")
list1 = [[5,6,7,8],[1,2,3,4]]
list2 = list1.copy()

list1[1][2] = 1000
print("Nested list1 by using copy() function: ",list1)
print("Nested list2 by using copy() function: ",list2)


# Now to resolve the issue we need the Deepcopy method 
print("------------------------Deep Copy----------------------------")
import copy 
list1 = [[5,6,7,8],[1,2,3,4]]
list2 = copy.deepcopy(list1)

list1[1][2] = 1000
print("DeepCopy list1 by using copy.deepcopy() function: ",list1)
print("DeepCopy list2 by using copy.deepcopy() function: ",list2)

# Deepcopy will work both with the 1D lists and multi dimensional lists 