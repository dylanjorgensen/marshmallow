
# Using map() you can map a function's return right into a list


a = range(1,11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def double(x):
    return x * 2

print 'List', a
print 'Mapped List:', map(double,a)


# Lambda also plays well with "map()"
# Now we don't even need to write out a func
result = map(lambda i:i**2,[1,3,6,8])
print result

