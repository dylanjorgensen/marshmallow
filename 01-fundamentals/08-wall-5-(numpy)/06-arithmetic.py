import numpy as np

'''
In addition to the standard arthimetic operations, Numpy also has a range of
other mathematical operations that you can apply to Numpy arrays, such as
mean and dot product.
'''


# 1D Array Arithmetic
if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    # print array_1 + array_2
    # print array_1 - array_2
    # print array_1 * array_2


# 2D Matrix Arithmetic
if False:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    # print array_1 + array_2
    # print array_1 - array_2
    # print array_1 * array_2


# Mixed Set Arithmetic
if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    array_3 = np.array([[6,2], [7,3], [8,2]], float)
    # print np.mean(array_1)
    # print np.mean(array_2)
    # print np.mean(array_3) # (4+5+5)/3


# Mixed Set Dot Product
# https://www.udacity.com/course/viewer#!/c-ud359-nd/l-4334619323/m-2951848662
if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([1, 2, 3], float)
    array_3 = np.array([[6], [7], [8]], float)
    array_4 = np.array([[6, 2], [7, 3], [8, 2]], float)
    # print np.dot(array_1, array_2) # 1+4+9
    # print np.dot(array_1, array_3) # 6+14+24
    # print np.dot(array_1, array_4) # 6+14+24, 2+6+6

# Scaler Multiplication
if True:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)
    # print a
    # print a*2
    # print a**2