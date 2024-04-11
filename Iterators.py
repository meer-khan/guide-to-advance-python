# declaring an iterable (list)


print("----------------iterables--------------------")
l1 = [1,2,3,4,5]

for i in range(len(l1)): 
    print(l1[i])

'''
we iterate over the iterable, using the for loop but the most important thing is,
iterable state cannot be stored and we cannot use the next() on iterable
'''


# Let's make the iterator out of the list we declared above "l1" using iter() object
print("-----------------Iterators-------------------")
l1= iter(l1)

for i in l1: 
    print(i)


print("--------------Check state/iteration saving of Iterator--------------")
l2 = [0,9,8,7,6,5]
l2_iterator = iter(l2)

for i in l2_iterator:
    print("inside loop: ",i)
    if i == 8:
        break

# this print statement should print "7"
print("outside loop: ",next(l2_iterator))
# this print statement should print "6"
print("outside loop: ",next(l2_iterator))
# As you can see in the output that we are getting the next elements of the 
# iterator from the ended execution of the loop.


'''
you can check that (by uncomminting the below code), we cannot use len() function 
and indexing on the iterator and we cannot use the next() on the iterables, 
'''


# l3 = [1,2,3]
# l3_iterator = iter(l3)

# # len() function check
# print(len(l3_iterator))

# # indexing check
# print(l3_iterator[0])

# # next() on iterable check
# print(next(l3))