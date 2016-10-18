import pandas as pd
import numpy as np

# Resources
# - http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
# - https://www.youtube.com/watch?t=679&v=1uVWjdAbgBg
# - http://nbviewer.ipython.org/github/twistedhardware/mltutorial/blob/master/notebooks/IPython-Tutorial/7%20-%20Pandas.ipynb

'''
You can think of Series as an one-dimensional object that is similar to
an array, list, column in a database or a vector in R or Matlab.

By default, a series will assign an index label to each item in the Series ranging from 0 to N, where N is
the number of items in the Series minus one.
'''

# --- Info & Printing --- #
if True:

    series = pd.Series([34,52,2,32,11,65,4])
    s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])

    type(series)
    type(s)
    series.astype(float)  # 'u8', 'float32', 'int32', 'float16', etc...
    series.astype('category')
    series.astype(np.float64)



