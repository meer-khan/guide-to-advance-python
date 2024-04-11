import numpy as np 
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,26,32,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000],
        "Date":["2014-04-31","2015-08-15","2013-09-23","2016-12-08","2022-11-11","1998-10-10","2002-05-25","2020-05-17"]}

dataset = pd.DataFrame(data)



#* __________________________________________SORTING_________________________________________________

# * Indexing of dataframe using the set_index method:
# You can move a column from the body of the DataFrame to the index. This is called "setting an index," 
# and it uses the set_index method. Notice that the output has changed slightly; 
# in particular, a quick visual clue that name is now in the index is that the 
# index values are left-aligned rather than right-aligned.
x = dataset.set_index(keys="Name")
print("\n1-Setting index of dataframe as Name:\n",x)
# Now we have set the index of dataframe as Name and whenever we apply the .loc attribute, it will be applied on the 
# Name column, Important thing is, Indexed column is always left aligned when we print the dataframe and 
# non-indexed columns are right aligned

print("\n2-Apply loc attribute:\n" , x.loc["Alice"])
# I passed the "Alice" to the loc, it will show all the records in which the Name is "Alice" but
# if I give it "Houston" from the City column, Pandas will throw an  error that this KeyError : "Houston"

#* Resetting indexes
# We can reset the index by appling the rest_index() method 
x = x.reset_index()
print("\n3-Resetting the index:\n", x)

print("\n4-Printing whole dataframe after resetting the index:\n",x)

# let's set the index again to continue our work:
x = dataset.set_index(keys="Name")

# we can alos drop the indexed column using the reset_index() function 
print("\n5-Dropping indexed column:\n", x.reset_index(drop=True))

# using indexing, we can simplify some tasks e.g.
# to get the values from the dataframe we  did something like this: 
print("\n6-Getting values from the dataframe in previous way:\n", dataset[dataset["Name"].isin(["Alice"])])

# we can do that task if the Name column is indexed in our dataframe by using the following syntax:
print("\n7-Getting value from the indexed column:\n", x.loc["Alice"])

# values in the index donot need to be unique, we can pass those columns as well that have duplicate values like "Salary" in our DF
x = dataset.set_index(keys="Salary")
print("\n8-Duplicated values column used as Index:\n", x)
# altough Name column alreadu has duplicated values like "Alice"


# * Multi Level Indexing OR Hierarchical Indexing: 
# we can do it by passing the list of coulmns to the "key" argument of set_index() function

x = dataset.set_index(keys=["Name", "Salary"])
# "Name" will be the Level1 and "Salary" will be considered as Level2 by Pandas
# "Salary" is nested inside the "Name" index 

# we can find Name "Alice" and "Mike" from the indexed column in multiindexing like this: 
print("\n9-Multi indexing, and subsetting on multiple values:\n", x.loc[["Alice","Mike"]])


# we can give the values for Both levels , Name and Salary in tuple
print("\n10-Multi indexing, and subsetting on both levels, Name and Salary:\n", x.loc[[("Alice",95000),("Mike",60000)]])



#* Sorting Indexes: 
# we can sort the indexes using the sort_index() function
# let's first reset the indexing and apply single index 
x = x.reset_index()

# Reindexing 
x = dataset.set_index(keys="Name")
print("\n11-Sorting the indexed column:\n", x.sort_index())

print("\n12-Sorting the indexed column in descinding order:\n", x.sort_index(ascending=False))


# Sorting on multi indexed or Hierarchical indexing: 

# resetting the index
x = x.reset_index()

# reindexing 
x = dataset.set_index(keys=["Name","Salary"])

print("\n13-Multiindex sorting:\n", x.sort_index(ascending=[False,True]))
# in this sorting pandas execute from lower to upper level, from Salary to the Name 
# Pandas first sort the Salary into Ascending order , and Than sort the Name in Descending order



# Mentioning levels: 
# by using the level parameter, we can define the levels on which the sorting take place 
# In line below, we have set level 1 on Salary and level 2 on Name 
# Pandas sort by lower to upper level 
# First Pandas will sort Name in descending order and than
# sort he Salary in ascending order
print("\n14-Multiindex sorting:\n", x.sort_index(level=["Salary", "Name"]   , ascending=[False,True]))





# * ______________________________________________ SLICING ______________________________________________________________

# Resetting the indexes: 
x = x.reset_index()

#* Use of iloc operator in pandas
# it is used to extract columns and rows on the basis of indexes of columns and rows 
print("\n15-First two rows of First 3 columns:\n", x.iloc[0:2,0:3])

print("\n16-First two rows of First 3 columns other syntax:\n", x.iloc[:2,:3])


# if the indexes are set we can do slicing using the loc operator
x = dataset.set_index(keys="Name")

# Below line will produce error, because loc slicing does not work on the columns that have duplicated values 
# So I am commenting this line 
# print("\n17-Slicing using loc operator on indexed dataframe:\n", x.loc["Alice":"Mike"])


# we can do it by using the City Column which is unique
x = dataset.set_index(keys="City")
print("\n17-Slicing using loc operator on indexed dataframe:\n", x.loc["Houston":"America"])
# In this slicing, America will be included, it will not be excluded

x = x.reset_index()
x = dataset.set_index(keys=["Age","City"]).sort_index()
#* IMPORTANT in slicing over the multi indexed DF using loc operator
# if we apply loc operator on the inner level of indexed columns ,
# Pandas will not throw any error, rather it will give only empty data frame 
# lets try

print("\n18- Slicing on multiindexed column of inner level:\n", x.loc["Houston":"America"]) 


# but we can apply the loc operator slicing on the upper level which is "Age"
print("\n19-Slicing on upper level of multiindexed DF:\n",x.loc[30:90])


# Slicing inner levels correctly, we give tuple , with colon
print("\n20-Slicing the multiindexed in correct way:\n", x.loc[(30,"Houston"):(90,"America")])


#* Slicing on coloumns using the loc operator
# Important thing to remeber, slicing on Indexed column and Slicing on non-indexed columns is different
# we cannot merge indexed column with the non-indexed column during column slicing like below
# im commenting this line, because it will generate error

# print("\n20-Slicing on coloumns using the loc operator\n", x.loc[:,"Name":"City"])


print("\n21-Slicing on coloumns using the loc operator\n", x.loc[:,"Name":"Salary"])

print(x)
# Getting specific columns from the slicing all levels of indexing
# *SLICE TWICE
# 1- Slice Age from 30 to 90 with City from Houston to America
# 2- Slice Column of Name and Salary only
print("\n22-Slicing the multiindexed in correct way:\n", x.loc[(30,"Houston"):(90,"America"),"Name":"Salary"])



# Resetting the indexes
x = x.reset_index()

# Indexed as date
x = x.set_index(keys="Date")
# ! not understood, require time to understand this slicing
print("\n23-Slicing on Date:\n", x.loc["2016-12-08":"2020-05-17"])

# This line is  giving error
# ! need to check
# print("\n24-Slicing on Date:\n", x.loc["2014":"2020"])






