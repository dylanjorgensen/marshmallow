
# What is the difference between range and xrange


# xrange is more efficient
# It evaluates lazily and acts like a generator
# xrange(x).__iter__()

xrange(1,20) # Fast




# range creates a list, where every element is stored in memory.

range(1,20) # = Bloated





