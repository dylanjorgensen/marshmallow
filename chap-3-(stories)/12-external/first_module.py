# https://www.youtube.com/watch?v=sugvnHA7ElY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=1


# When ran from this file we get __name__ == '__main__'
# When ran from second_module we get __name__ == first_module

print "First modules Name: {}   ".format(__name__)



# So by checking if __name__ is equal to '__main__'
# We are asking, "Is this file being ran directly by python"
# Or, "Is this file being imported"

# Will only print when ran directly
if __name__ == '__main__':
    print 'I live in first_module and am being ran directly :)'

# Will only print when imported
if __name__ == 'first_module':
    print 'I live in first_module but am being IMPORTED!! :('



def unlock_tupperware():
    print "apple slices"


