import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,26,32,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000],
        "Date":["2014-04-31","2015-08-15","2013-09-23","2016-12-08","2022-11-11","1998-10-10","2002-05-25","2020-05-17"]}

dataset = pd.DataFrame(data)


# .isna() function to check the whole dataset into the binary format, either any values in the 
# dataset is missing or not

print(dataset.isna())

# but this approach is not much helpful when dealing with large dataset 
# for large dataset we can see the columns, if any column has missing value of not 

print(dataset.isna().any())



# *Sum of missing values in the column
print(dataset.isna().sum())



# Dropping the rows that have missing values
print(dataset.dropna())


# Filling missing values to some value
print(dataset.fillna(0))
