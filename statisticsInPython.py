# import pandas as pd 
# import numpy as np 



# sleep_data = pd.DataFrame({
#     'Country': ['Belgium', 'USA', 'Belgium', 'USA'],
#     'sleep_time': [7, 6, 8, 7]
# })

# print(sleep_data["Country"] == "Belgium" , "sleep_time")


import pandas as pd

# Creating the sleep_data DataFrame
sleep_data = pd.DataFrame({
    'Country': ['Belgium', 'USA', 'Belgium', 'USA'],
    'sleep_time': [7, 6, 8, 7]
})

# Selecting the 'sleep_time' column for 'Belgium' only
# be_sleep_time = sleep_data.loc[sleep_data['Country'] == 'Belgium', 'sleep_time']
# print(be_sleep_time)

be = sleep_data[sleep_data["Country"]== "Belgium"]
print(be["sleep_time"])