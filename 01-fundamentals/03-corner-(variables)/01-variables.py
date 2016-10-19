
example_string = 'hello world'


# Invoke the built-in help system.
# help()  # help([object])

# Without arguments, return the list of objects in the current namespace.
print dir()  # dir([object])

#  With an argument, attempt to return a list of valid attributes/methods for that object.
print dir(example_string)

# iobject = 'magic 8ball'
print id(example_string)  # id(object)

# Return class/type of object
type()  # type(object)