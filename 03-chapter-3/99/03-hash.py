
# ordinal "ord()" gives us a way to turn a string into a number
# only works on single letters
print ord('a')
print ord('A')
print ord('B')
print ord('b')


# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        # ord() then modulo make unique hash
        h = h + ord(c)% buckets
    return h

print hash_string('a', 12)
print hash_string('dylan', 100)






#print hash_string('a',12)
#>>> 1

#print hash_string('b',12)
#>>> 2

#print hash_string('a',13)
#>>> 6

#print hash_string('au',12)
#>>> 10

#print hash_string('udacity',12)
#>>> 11
