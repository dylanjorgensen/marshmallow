# https://docs.python.org/2/library/collections.html


from collections import Counter


exampleList = [1,2,34,2,1,2,4,2,21,4,12,3,2,2,1,2,2,4]

counts = Counter(exampleList)

print counts[2]
print counts
