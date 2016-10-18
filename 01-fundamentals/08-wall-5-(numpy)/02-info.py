import numpy as np

data_set = np.array([[ 0.99101817,  0.91362334,  0.37546237],
                     [ 0.66962595,  0.27485988,  0.45081456]])


# Info
ds = np.arange(1,10,2)
ds.ndim  # Returns the dimensions of the array
ds.shape  # Displays shape size
ds.size  # Returns the number of elements in array


# Memory usage
ds.dtype
ds.itemsize  # Returs how many bits of memory they elements each use
ds.size * ds.itemsize  # Total memory usage


# Max and min
np.max(data_set)
np.max(data_set, axis=0)  # Rows
np.max(data_set, axis=1)  # Columns
np.min(data_set)


# Central tendency
np.mean(data_set)
np.median(data_set)
np.std(data_set)
np.sum(data_set)