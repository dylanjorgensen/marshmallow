import pandas as pd


# --- Auto Index --- #

# Series with an auto generated int index
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    #print series



# --- Specific Index --- #
# Series with custom indices
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    # print series



# --- From List --- #
my_list = [1,2,3,4,5,6]
s = pd.Series(my_list)
# print s



# --- From Dictionary --- #

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
# print cities
