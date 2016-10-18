# This will go into the specified directry and print out
# the names of any jpg files it finds.



import os, glob


for file in glob.glob("*.png"):
    print file