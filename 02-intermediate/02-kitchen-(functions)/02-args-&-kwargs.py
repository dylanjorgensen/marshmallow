# You  use *args when you're not sure how many arguments might be passed to your function. i.e. it allows you pass an arbitrary number of arguments to your function. For example:


# *Args
def print_everything(*args):
    for count, i in enumerate(args):
        print '{0}. {1}'.format(count, i)

print_everything('apple', 'banana', 'cabbage')


# **kwargs
def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)

table_things(apple = 'fruit', cabbage = 'vegetable')






'''
It is possible to declare functions which receive a variable number of arguments,
using the following syntax:
'''

if False:

    def foo(first, second, third, *therest):
        print "First: %s" % first
        print "Second: %s" % second
        print "Third: %s" % third
        print "And all the rest... %s" % list(therest)

    foo('uno', 'dos', 'thres', 'yap', 'yip', 'yup')


'''
- It is also possible to send functions arguments by keyword, so that the order of the argument
does not matter, using the following syntax:
'''

if True:
    def bar(first, second, third, **options):
        if options.get("action") == "sum":  # Notice the .get method that matches the param input
            print "The sum is: %d" % (first + second + third)

        if options.get("number") == "first":
            return first

    result = bar(1, 2, 3, action = "sum", number = "first")
    print "Result: %d" % result