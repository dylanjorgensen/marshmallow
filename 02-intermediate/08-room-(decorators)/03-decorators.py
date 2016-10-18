"""
- Methods are associated with object instances or classes; functions aren't.
- When Python dispatches (calls) a method, it binds the first parameter of that call to the appropriate object reference.
- For most methods that's conventionally called self.
"""

# Normal function

def foo_func(a,b):
    return a+b

print foo_func(3,4)



# --- Normal Methods --- #
# Notice that I call it with my (pair of) arguments, but I defined it with three parameters.
# The dispatch inserts the reference to "self" into the argument list.

class FooClass(object):
    def foo(self,a,b):
        self.contents = a-b
        return self.contents


instance = FooClass()
print instance.foo(1,2)




# --- Static Methods --- #
# Note that we don't need to instantiate a Bar() object to access the .foo() static method.
# Static methods are basically just a way to organize function into the name space


class Bar(object):
    @staticmethod
    def foo(a,b):
        return a+b

print 'static method', Bar.foo(1,2)

