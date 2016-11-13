

# --- Reduce --- #
# Reduce requires a function that takes 2 parameters
# It starts processing with the first two elements...
# Then uses that result, as the first parameter and next element for the second
# You also have the option to seed the second parameter


a = range(1,11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum(x, y):
    return x + y

print 'Reduced List:', reduce(sum, a)
print 'Reduced List:', reduce(sum, a, 100)




# Flatten a list
# Goal: turn [[1, 2, 3], [4, 5], [6, 7, 8]] into [1, 2, 3, 4, 5, 6, 7, 8].
print reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], [])


# List of digits to a number
# Goal: turn [1, 2, 3, 4, 5, 6, 7, 8] into 12345678.
reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7,8], 0)


# Find the intersection of N given lists:
input_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
result = reduce(set.intersection, map(set, input_list))