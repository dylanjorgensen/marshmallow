



def reverse(data):
    # First -1 is to stay in len of data
    # Second -1 is go out of bounds
    # Third -1 is go down in increments of 1
    for i in range(len(data)-1,-1,-1):
        # Yield is a pause with a conditional return
        yield data[i]


def main_func():
    rev = reverse('dylan')
    for char in rev:
        print char


print main_func()




# --- Generator Expression --- #

name = 'dylan'
print 'generator', list(name[i] for i in range(len(name)-1,-1,-1))