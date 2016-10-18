# Functions in python are said to be first-class citizens
# They can be passed into other functions, stored as variables and returned from functions.


def foo_bar(x,y):
    return x+y


# Print un-nested function
print foo_bar(1,1)


# Nest func without parameters into new var
foo_var1 = foo_bar

print foo_var1  # No error but will throw func ID
print foo_var1(2,2)  # Can add vars later


# Nest func with parameters
foo_var2 = foo_bar(3,3)  # with parameters

print foo_var2
#print foo_var2(4,4)  # Error: Can't overwrite