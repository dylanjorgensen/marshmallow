import numpy as np


data_set = np.array([[ 0.99101817,  0.91362334,  0.37546237],
                     [ 0.66962595,  0.27485988,  0.45081456]])

# Shape Info
print data_set.shape  # 2 rows, 3 columns



# Reshape
np.reshape(data_set, (3,2))  # 3 rows, 2 columns
np.reshape(data_set, (6,1))  # 6 rows, 1 column
np.reshape(data_set, (6))  # The individual int will remove the second dimension
np.ravel(data_set)  # Flattens all dimensions


# Transposing an array
np.transpose(data_set)


