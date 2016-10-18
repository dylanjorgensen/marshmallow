import pandas as pd

# --- Slicing --- #

# Specific range with auto-indexed
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print series[2:4]

# Specific items from string indexing
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print series['Instructor']
    print series[['Instructor', 'Curriculum Manager', 'Course Number']]

# Boolean parameters indexing
if False:
    series_cuteness = pd.Series([1, 2, 3, 4, 5, 6], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten', 'cow'])
    print series_cuteness > 3
    print series_cuteness[series_cuteness > 3]

# Finding a Null (Requires Numpy import)
if False:
    series_cuteness = pd.Series([1, 2, 3, 4, np.NaN, 6], index=['Cockroach', 'Fish', 'Mini Pig','Puppy', 'Kitten', 'cow'])
    print series_cuteness[series_cuteness.isnull()]




# --- Manipulation --- #

# Built in functions pd has for changing data on the fly
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001,],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    series[series < 500] = 'cow'
    series[series == 9001] = 'chicken'

    # Scalars
    series_cuteness = pd.Series([1, 2, 3, 4, 5, 6], index=['Cockroach', 'Fish', 'Mini Pig','Puppy', 'Kitten', 'cow'])

    print series_cuteness * 3




# --- Booleans --- #
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    series = series > 2
    series.any()  # Only works after the inequality was checked




# --- Functions --- #
if False:
    x = pd.Series([1,2,3,4,5])
    def f(x):
        if x % 2 == 0:
            return x * 2
        else:
            return x * 3

    print x.apply(f)

