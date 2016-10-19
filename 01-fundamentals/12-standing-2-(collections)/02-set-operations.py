
# Sets can be specified by passing in a list into the set class
digit_list = [1,2,3,4,5,6]
odd_list = [1,3,5,7,9,11]

# Unlike lists and tuples a set does not care about order
digit_set = set(digit_list)
odd_set = set(odd_list)

# Sets are useful because they provide set operations, such as
# union ( | ), intersection (&), difference (-), and x or (^).
even_set = digit_set - odd_set
union_set = digit_set | odd_set
print even_set
print union_set
