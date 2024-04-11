import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np



data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,26,32,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000],
        "Date":["2014-04-31","2015-08-15","2013-09-23","2016-12-08","2022-11-11","1998-10-10","2002-05-25","2020-05-17"]}

dataset = pd.DataFrame(data)

#* hist() function will give histogram 
# x axis conatains the salaries 
# y axis represents the number of people in each salary range
dataset["Salary"].hist()
plt.show()


#* We can adjust the number of bars, 
# or bins, using the "bins" argument. Increasing or decreasing this can 
# give us a better idea of what the distribution looks like

dataset["Salary"].hist(bins=20)
plt.show()


# Grouping by the columns to get the bar plots 
x = dataset.groupby("Name")["Salary"].mean()
x.plot(kind="bar", title="Salary Bars")
plt.show()


#* line charts are best to describe the data over the period of time 
# e.g. increase or decrease in weight of human over period of 5 years
# currently we dont have that type of data so I am applying it on our current DF
dataset.plot(x="Age",y="Salary",kind="line", title="line chart of salaries and age")
plt.show()

df = pd.DataFrame(
    {
   'pig': [20, 18, 489, 675, 1776],
   'horse': [4, 25, 281, 600, 1900],
   "period":[1990, 1997, 2003, 2009, 2014]
   }
   )

# print(df.plot.line())
df.plot(x="period",y="horse",kind="line", title="line chart of salaries and age", rot=45)
plt.show()



#* Scatter plots are great for visualizing relationships between two numeric variables. 
# To plot each dog's height versus their weight, we call the plot method
dataset.plot(kind="scatter", x="Age", y="Salary",title="Age and salary Scatter plot")
plt.show()


# * Layering graphs. 
dataset[dataset["Gender"]=="F"]["Age"].hist()
dataset[dataset["Gender"]=="M"]["Age"].hist()
plt.legend(["F","M"])
plt.show()

# Let's fix this problem by making the histograms translucent. We can use hist's 
# alpha argument, which takes a number. 0 means completely transparent that is, 
# invisible, and 1 means completely opaque.
dataset[dataset["Gender"]=="F"]["Age"].hist(alpha=0.7)
dataset[dataset["Gender"]=="M"]["Age"].hist()
plt.legend(["F","M"])
plt.show()

