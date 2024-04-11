import pandas as pd
import numpy as np

data = {"date": ["2018-01-01", "2018-02-01", "2019-01-01", "2019-02-01"],
        "temperature": [20, 25, 18, 22]}
df = pd.DataFrame(data)


data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Alice', "Mike","Alice", "Alice"],
        'Age': [25, 30, 35, 40, 45,25,30,90],
        'Gender': ['F', 'M', 'M', 'M', 'F',"F","M","F"],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',"America","Chicago","Lahore"],
        'Salary': [60000, 60000, 70000, 80000, 95000,60000,60000,60000]}

dataset = pd.DataFrame(data2)


# Extract year from date column
df["year"] = pd.DatetimeIndex(df["date"]).year

# Show the updated dataframe
print(df)



# * Taking mean of whole column
x = dataset["Salary"].mean()
print("\nMean of Salary is:\n", x)

# * Taking median of whole column
x = dataset["Salary"].median()
print("\nMedian of Salary is:\n", x)

# * Taking mode of whole column
x = dataset["Salary"].mode()
print("\nMode of Salary is:\n", x)

# * Taking sum of whole column
x = dataset["Salary"].sum()
print("\nSum of Salary is:\n", x)

# * Taking min of whole column
x = dataset["Salary"].min()
print("\nMin of Salary is:\n", x)

# * Taking max of whole column
x = dataset["Salary"].max()
print("\nMax of Salary is:\n", x)

# * Taking quantile of whole column
x = dataset["Salary"].quantile(.20)
print("\nQuantile of Salary is:\n", x)

# * Taking cumulativeSum of whole column
x = dataset["Salary"].cumsum()
print("\nCumulative Sum of Salary is:\n", x)

# * Taking Cumulative Product of whole column
x = dataset["Salary"].cumprod()
print("\nCumulative Product of Salary is:\n", x)

# * Taking cumulative Min of whole column
x = dataset["Salary"].cummin()
print("\nCumulative Min of Salary is:\n", x)

# * Taking cumulative Max of whole column
x = dataset["Salary"].cummax()
print("\nCumulative Max of Salary is:\n", x)




# TODO: ________________________________________________ agg() FUNCTION: _______________________________________________________________
# The aggregate, or agg, method allows you to compute custom summary statistics. 
# Here, we create a function called pct30 that computes the thirtieth percentile of a DataFrame column

def pct30(column):
    return column.quantile(0.3)

def pct40(column):
    return column.quantile(0.4)

x = dataset["Salary"].agg(pct30)
print("\n Agg() function on salary column:\n",x)
# agg() function can also be use for multiple columns
x = dataset[["Age","Salary"]].agg(pct30)
print("\n Agg() function on multiple columns age and salary:\n",x)

# We can pass multiple functions to agg function as well 
x = dataset["Salary"].agg([pct40,pct30])
print("\n Agg() function can accept multiple functions: \n",x)

# TODO: need to be check
# ! agg function cannot accept multiple functions with mulitple columns 



# *Dropping duplicates: 
x = dataset["Salary"].drop_duplicates()
print("\n Dropped duplicate value of 60000 from the Salary Column:\n",x)

# * 2nd Syntax of dropping duplicates: 
# This syntax will return the whole dataset
print("\n 2nd syntax for Dropped duplicate value of 60000 from the Salary Column:\n", dataset.drop_duplicates(subset="Salary"))
# As you can see from the output that, There are 3 girls named with alice SO,
# We can also apply the dropduplicates on multiple columns
# Below syntax will drop the duplicat only where Name and Salary match in same record
# If name is Alice and Salary is 50000, and Name is Alice and Salary 60000, These are not duplicates 
# They have difference values for columns matched in the dropduplicates column
print("\n dropping duplicate from multiple columns Salary and Name:\n", dataset.drop_duplicates(subset=["Name","Salary"]))
x = dataset[["Name","Salary"]].drop_duplicates()
print("\n 2nd syntax od dropping multiple columns that are duplicates, and it will return only the those columns that we have mentioned for the dropping duplicates:\n",x)

# ____________________________________________________________________________________________________________
# *Counting Values in dataframe
# value_counts() function will count the values appearing how many times in the column we mentioned 
# e.g. we have 3 Alice names in our dataframe and we will apply value_counts() function to check the count of each name

x = dataset["Name"].value_counts()
print("\nCount of Name using value_conuts()\n",x)

# we can also sort the results of value counts

x = dataset["Name"].value_counts(sort=True)
print("\nSorted values of Count of Name using value_conuts()\n",x)

#* The normalize argument of value_counts() function can be used to turn the counts into 
# proportions of the total. 25% of the dogs that go to this vet are Labradors.
x = dataset["Name"].value_counts(sort=True,normalize=True)
print("\nNormalized and Sorted values of Count of Name using value_conuts()\n",x)



# _____________________________________________________________________________________________________________
# * While computing summary statistics of entire columns may be useful, 
# you can gain many insights from summaries of individual groups. 
# For example, does one color of dog weigh more than another on average? Are female dogs taller than males

# Pandas groupby is used for grouping the data according to the categories and 
# apply a function to the categories. It also helps to aggregate data efficiently

# if we do this, pandas will return the group by object
x = dataset.groupby("Name")["Salary"].mean()
print("\nGroupby function of pandas, applied on the Name and compute the 'mean' of the salary", x)
# What it does is, It will create a group of "Alice" because "Alice" occurs 3 times in our dataframe 
# Takeout the salaries of "Alice" and apply mean on her salary. 

#* groupby on multiple columns:
print(dataset)

# *IMPORTANT group by also removes the 
x = dataset.groupby(["Name","Age"])
print(x.first)
# ! Still confused why first() method is working here
# When having a DataFrame with dates as index, this function can select the first few rows based on a date offset


# We can also use the agg() function to apply multiple functions on the groupedby data 
x = dataset.groupby("Name")["Salary"].agg([min,max,sum])
print("\nApplied multiple functions in agg() method on the dataframe after groupping by\n", x)


# * Grouping by multiple columns 
x = dataset.groupby(["Gender","Name"])["Salary"].mean()
print("\nGroupping by multiple columns and calculate mean on salary\n", x)

x = dataset.groupby(["Age","Name"])["Salary"].mean()
print("\nGroupping by multiple columns, AGE AND NAME\n", x)


# *Grouping by multiple coulmns and apply multiple functions using agg()
x = dataset.groupby(["Gender","Name"])["Salary"].agg([min,max,sum])
print("\nGroupping by multiple columns and calculate min max and sum using agg()\n", x)
# *IMPORTANT: if we are doing groupby on multiple columns and 
# we have a record in the dataframe where those multiple column(on which we are applying the groupinhg)
# are exactly same, Pandas will return us 1 entry of it instead of multiple entries, pandas is not droping those records, 
# but it applies summarize function on every record and returns just 1 record of it


# ___________________________________________________________________________________________________

# * Pivot_Table function: 
# the things we did with the groupby function we can do it through the pivot function as well. 
# BY default pivot_table() function applies the mean function but we can change it using the aggfunc argument

print("\n Application of pivot_table() function on index Name and value Gender\n",dataset.pivot_table(values="Salary", index="Name"))


print("\npivot_table() on on multiple columns to group\n",dataset.pivot_table(values="Salary", index=["Name","Gender"]))


print("\npivot_table() on on multiple indexes (summarize tables) to group\n",dataset.pivot_table(values=["Salary","Age"], index=["Name","Gender"]))

print("\npivot_table() on on multiple indexes (summarize tables) to group\n",dataset.pivot_table(values=["Salary","Age"], index=["Name","Gender"]))


# Using column parameter will return dataframe that have all the columns of the sequence that we passed in the columns paramter
# and give nan value if value doesnot exist
# ! NOT UNDERSTOOD

# *STOOD STOOD , I GOT IT, Here's the explanation:
# index column is used to group by and display in rows and 
# column argument is used to groupby and display in columns

print("\npivot_table() on multiple indexes (summarize tables) to group by using columns argument\n",dataset.pivot_table(values="Salary", index="Name",columns=["Age","City"]))

# we can fill the value using the fill_value parameter to replace the Nan with some value
print("\npivot_table() filled missing values with 0\n",dataset.pivot_table(values="Salary", index="Name",columns=["Age","City"], fill_value=0))

# margin parameter set to true will result in additional column "All" and row at the last that will show the mean
# of the whole row and column
print("\npivot_table() filled missing values with 0\n",dataset.pivot_table(values="Salary", index="Name",columns=["Age","City"], fill_value=0, margins=True))

# Application of aggfunc
print("\npivot_table() aggfunc parameter to apply median\n",dataset.pivot_table(values=["Salary","Age"], index=["Name","Gender"], aggfunc=np.median))

# apply multiple aggregation function by passing the list of numpy function to the aggfunc parameter
print("\npivot_table() aggfunc parameter to apply median and mean\n",dataset.pivot_table(values=["Salary","Age"], index=["Name","Gender"], aggfunc=[np.median, np.mean]))