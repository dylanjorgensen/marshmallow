import numpy as np

# Resources
# - https://rorasa.wordpress.com/2012/05/13/l0-norm-l1-norm-l2-norm-l-infinity-norm/
# - http://www.researchgate.net/publication/266617010_NumPy__SciPy_Recipes_for_Data_Science_Squared_Euclidean_Distance_Matrices


'''
These are some things I was experimenting with from my linear algebra class
'''


# Euclidean Norms
if True:
    a = np.array([2,-4,5,-2])
    print np.linalg.norm(a) # Squares and adds each value then takes the square root


if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([2, 3, 4, 5])
    print np.linalg.norm((a - b), ord=1)

    c = np.arange(15).reshape(5,3)
    print np.linalg.norm(c, axis=1)


    z = np.array([complex(c.m_x, c.m_y) for c in cells])
    print z