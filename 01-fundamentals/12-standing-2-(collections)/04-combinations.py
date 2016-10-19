# https://www.youtube.com/watch?v=QI9EczPQzPQ

import itertools

my_list = [1,2,3]


# The order does not matter with combinations
combinations = itertools.combinations(my_list, 2)  # Groups of 2
for c in combinations:
    print c

