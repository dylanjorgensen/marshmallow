
import numpy as np

from random import choice



training_data = [ (np.array([0,0,1]), 0),
                  (np.array([0,1,1]), 1),
                  (np.array([1,0,1]), 1),
                  (np.array([1,1,1]), 1), ]


w = np.random.rand(3)

x, expected = choice(training_data)
print(x)
print(expected)