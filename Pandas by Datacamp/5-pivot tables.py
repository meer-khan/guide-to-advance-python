import numpy as np 
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,26,32,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000],
        "Date":["2014-04-31","2015-08-15","2013-09-23","2016-12-08","2022-11-11","1998-10-10","2002-05-25","2020-05-17"]}

dataset = pd.DataFrame(data)


# *Pivot tables are just dataframes with sorted indexes, that means 
# all the things we have learned so for in slicing and aggregaing the data 
# can also be used on the pivot tables


# by default pivot tables apply mean summarizatin function on the values argument column
x = dataset.pivot_table(values="Salary", index="Name", columns="Age")
# if I apply slicing from Bob to Alice, Pandas will give empty data frame 
# because there are multiple Alice Names after the Bob Name
# So I sliced the pivot table from Bob to Dave where there is no 
# duplication of any name
print("\n1-Slicing on pivot tables:\n",x.loc["Bob":"Dave"])

# mean() function on the pivot table dataframe applies mean by default on the index column
# * index column is the column that we have passed in the values argument of the pivot_table() function
# index column is used to group by and display in rows and 
# column argument is used to groupby and display in columns

# behaviour of the line below will be same if we donot specify the axis argument
# * Here the mean is calculated for each Age which is  across the Salary
print("\n2-Mean on index table:\n",x.mean(axis="index"))

# let's change the axis to columns
# Here mean is calculated for each row(which is Name) across the Salary
print("\n3-Mean on columns table:\n",x.mean(axis="columns"))




