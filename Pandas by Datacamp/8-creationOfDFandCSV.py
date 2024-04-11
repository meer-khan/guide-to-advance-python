import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



#* There are two ways to create the Dataframe
# 1- From dictionary of lists
# 2- From list of dictionaries


# *This is dictionary of lists
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,26,32,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000],
        "Date":["2014-04-31","2015-08-15","2013-09-23","2016-12-08","2022-11-11","1998-10-10","2002-05-25","2020-05-17"]}

dataset = pd.DataFrame(data)
print(dataset)


# *This is list of dictionaries
data = [{"Name":"Alice", "Age":25, "Gender":"F", "City":"NewYork", "Salary":60000, "Date":"2014-04-31"},
        {"Name":"Mike", "Age":30, "Gender":"F", "City":"NewYork", "Salary":65000, "Date":"2014-04-31"},
        {"Name":"Charles", "Age":35, "Gender":"F", "City":"NewYork", "Salary":90000, "Date":"2014-04-31"}]

dataset = pd.DataFrame(data)
print(dataset)



# _____________________________________ CSV________________________________________
# CSV, or comma-separated values, is a common data storage file type. 
# It's designed to store tabular data, just like a pandas DataFrame. It's a text file, 
# where each row of data has its own line, and each value is separated by a comma. Almost every database, 
# programming language, and piece of data analysis software can read and write CSV files.
# That makes it a good storage format if you need to share your data 
# with other people who may be using different tools than you.

# pd.read_csv() this function is used to read the data from the csv
# pd.to_csv() this function is used to write data into the csv