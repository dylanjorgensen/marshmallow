

p = 'hello'
ps = p
m = 'hello'
n = 'hellos'


# is evaluates to True if the variables on either side of the operator point to the same object and False otherwise

print ps is p
print ps is m
print ps is n


# is not evaluates to False if the variables on either side of the operator point to the same object and True otherwise

print ps is not p
print ps is not m
print ps is not n



# The not keyword can also be used to inverse a boolean type.
print not False