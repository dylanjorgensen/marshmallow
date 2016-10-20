

my_list = [1,2,2,2,2,3,4,5,6,7,8,9]

# When making a set the duplicates will be removed
my_set = set(my_list)

my_set2 = {1,2,2,3,4,5,6}

print(my_set)
print(my_set2)


'''
-Sets are lists with no duplicate entries. Let's say you want to collect
a list of words used in a paragraph:
'''

print set("my name is Eric and Eric is my name".split())

'''
- This will print out a list containing "my", "name", "is", "Eric", and finally "and". Since the rest
of the sentence uses words which are already in the set, they are not inserted twice.

- Sets are a powerful tool in Python since they have the ability to calculate differences
and intersections between other sets. For example, say you have a list of participants in
events A and B:
'''

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended both events, you may use the "intersection" method:
print a.intersection(b)
print b.intersection(a)

# To find out which members attended only one of the events, use the "symmetric_difference" method:
print a.symmetric_difference(b)
print b.symmetric_difference(a)

# To find out which members attended only one event and not the other, use the "difference" method:
print a.difference(b)
print b.difference(a)

# To receive a list of all participants, use the "union" method:
print a.union(b)