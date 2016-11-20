
# List comprehension form (returns list) because of BRACKETS
my_nums = [x*x for x in [1,2,3,4,5]]
print type(my_nums) # list object
print my_nums




# Generator comprehension form (returns generator) because of PARENTHESIS
my_nums = (x*x for x in [1,2,3,4,5])
print type(my_nums) # generator object
print my_nums



# List --> Generator casting & visa versa.
print "list", list(my_nums) # Convert generator to list (looses performance)
print "iter", iter(my_nums) # convert list to generator
