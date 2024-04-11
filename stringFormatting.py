''' 
Formatting with % operator: we can append the value in string by using 
%s , %d , %f , and %b for strings, integers, floats, and binaries respectively. 

'''

varStr = "Beautiful"
varInt = 123
varFloat = 1.22

print("---------------%operator----------------")
print("Hello %s World!"%varStr)
print("Integer is %d"%varInt)
print("Float is %f"%varFloat)

# f-string or string literal 
# write the variable in curly brackets and type f before the string

print("----------------f-string----------------")
print(f"Hello {varStr} World!")
print(f"Integer is {varInt}")
print(f"Float is {varFloat}")

# write empty curly brackets inside string and insert all variables in order 
# in the format function to place in the respective curly brackets

print("--------------format function -----------")
print("Hello {} World!".format(varStr))
print("Integer is {}".format(varInt))
print("Float is {}".format(varFloat))
print("Multiple variables like: {} {} {} in the string".format(varStr,varInt,varFloat))



print(dir(int))
