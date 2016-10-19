import pandas as pd
import numpy as np

# Resources
# - https://www.youtube.com/watch?v=1uVWjdAbgBg

'''
- Think of DataFrame similar to a row and column spreadsheet but formed from a group of series arrays
- Remember indexes are NOT columns because you cant select an entire column.
- If you get an "copy" error your might need to add "inplace=True" as a parameter
'''

# print df.dtypes  # Returns column headers and types
# print list(df.index.values)  # Returns rows index
# print list(df.columns.values)  # Returns column headers

df_survivors = df.ix[:,['PassengerId', 'Survived']]


# Data frame printing
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    # print football
    # print football.head() # Displays the first five rows of the dataset
    # print football.tail() # Displays the last five rows of the dataset


# Retrieve info ABOUT a data frame
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)

    # print football.info() # Column totals and data types
    # print football.describe() # Count, mean, std, min, quartiles and max for ints.
    # print football.dtypes # To get the datatype for each column
