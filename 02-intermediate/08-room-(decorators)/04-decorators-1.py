# What I learned..
# - The *args and **kwargs lets the

# https://www.youtube.com/watch?v=9oyr0mocZTg

def my_decorator(wrapped):
    def inner(*args, **kwargs):
        return wrapped(*args, **kwargs)
    return inner


# Think of @my_decorator like an alias
# That resolves to: myfunc = my_decorator(myfunc)


@my_decorator # myfunc = my_decorator(myfunc)
def myfunc():
    pass
