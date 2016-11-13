# https://www.youtube.com/watch?v=ve2pmm5JqmI&index=12&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU



import os

# TIP* Drag the folder into terminal to get the URI
# os.chdir('/Users/dylanjorgensen/Dropbox/python/03-advanced/')

print os.getcwd()

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    print f.extend(dirpath)
    break