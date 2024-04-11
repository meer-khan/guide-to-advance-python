# Using range() function 

nums = range(0,10)
# it will give us the range object which we can convert into list object
print("Type of nums which is storing the range function: ",type(nums))
# what is actually stored in the nums
print("What is actually stored in the nums: ", nums)
# converting the nums into list object
listOfNums = list(nums)
# How it looks like after converting it into list
print(listOfNums) 


# Map function
def map_test(l1_element,str1_element,str2_element):
    # converting l1_element into string because it is in interger datatype
    return str(l1_element)+str1_element+str2_element

l1 = [1,2,3,4,5.6]
str1="This is string"
str2="minimum len"
result = map(map_test, l1,str1,str2)
print(list(result))

