import itertools as it
 
# defining the grouper function
def grouper(inputs, n, fillvalue = None):
    print("inputs",inputs)
    print("n",n)
    print("fillvalue",fillvalue)
    iters = [iter(inputs)] * n
    # print(iters)
    # print(len(iter))
    return it.zip_longest(*iters, fillvalue = fillvalue)
 
alpha = ['g', 'e', 'e', 'k', 's', 'f', 'o',
         'r', 'g', 'e', 'e', 'k', 's']
print(list(grouper(alpha, 3)))


colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors = iter(colors)
# print(colors)
# for i in colors:
    # print(i)
shapes = ['circle', 'triangle', 'square', 'pentagon']
result = it.chain(colors, shapes)
# print(result)
# for each in result:
    # print(each)
print(6<5)

# data = [1, 2, 3, 4, 6, 7, 8, 9, 10, 1,4,5,6,7]
# result = it.dropwhile(lambda x: x<5, data)
# for each in result:
#     print(each)