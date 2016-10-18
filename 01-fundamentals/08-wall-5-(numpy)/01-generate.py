
import numpy as np


# Create
np.array([2,3,4])
np.array([[1, 2, 3], [4, 5, 6]], float) # Multi-dimensional array


# List Generation
np.arange(12)  # [0  1  2  3  4  5  6  7  8  9 10 11]
np.arange(15,30)  # [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]
np.arange(1,4, 0.5)  # [1.   1.5  2.   2.5  3.   3.5]
np.arange(1,10, 2, dtype=np.float64)


# Matrix Generation
np.zeros( (3,4) )  # 3,4 specifies the shape
np.ones( (2,3,4))
np.empty( (2,3) ) # This puts random floats in as placeholders

np.linspace(15,30)  # Difference is in float type and final number
np.linspace(0,2,num=4)

np.random.random_sample((2,3))  # Params matrix shape, all values between 0-1





