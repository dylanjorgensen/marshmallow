# What I learned
# - We use *args, **kwargs to make decorators more flexible

# https://www.youtube.com/watch?v=9oyr0mocZTg

def shout(wrapped):
    def inner(*args, **kwargs):
        print 'BEFORE!'
        ret = wrapped(*args, **kwargs)
        print 'AFTER!'
        return ret
    return inner


@shout
def myfunc():
    print "hello"


myfunc()