import numpy as np

d1 = np.array([1, 2, 3, 4, 5], float)

# 1D Slicing
d1
d1[1]
d1[:2] # Range from 0-2


data_set = np.random.random((5,10))
data_set.shape  # Shape (5, 10)


# 2D Slicing
data_set[1]  # Returns full row/item
data_set[1][0]  # Returns individual value (Shorthand: data_set[1,0])

data_set[2:4]  # Returns full row 2 and 3
data_set[2:4,0]  # Returns only the 0th value in item/row 2 and 3
data_set[2:4,0:2]  # Similar to above returns 2 values from each of the 2 rows
data_set[:,0]  # Returns first value from each item


# 2D Stepping
data_set[2:4:1]
data_set[::]
data_set[::2]
data_set[2:4]
data_set[2:4,::2]  # Here we are stepping to the second dimension