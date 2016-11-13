# https://www.youtube.com/watch?v=fVon4QaY4wo

def add_one(myFunc):
    def add_one_inside():
        return myFunc + 1
    return add_one_inside

def old_func():
    return 3


print old_func()

composite_func = add_one(old_func)
print composite_func()