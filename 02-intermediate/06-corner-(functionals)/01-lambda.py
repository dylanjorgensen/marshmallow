# Lambda = function written in one line.

# Python supports a style of programming called functional programming where you can pass functions to other functions.
# The processing must be done on a single line to work.
# They are sometimes called anonymous functions because they have no name and are not bound to an identifier.




# Separated function with 1 parameters style
f = lambda x: x**2 + 2*x - 5
print("f is", f(2))

# def f(x):
#     x = x ** 2 + 2 * x - 5
#     print (x)
# f(2)


# set a default value for x
unit_step = lambda x: 0 if x < 0 else 1
hi = unit_step(-1)
print(hi)

# Separated function with 2 parameters style
one_line_func = lambda x, y : x*y
#print 'Simple Lambda', one_line_func(3,10)




# Lambda functions CAN NOT process lists
a = range(1,10)
b = range(11,20)
# print one_line_func(a,b) # Throws error




# If you need a list, lambda also plays well with "map()"
result = map(lambda i:i**2,[1,3,6,8])
# print(result)


