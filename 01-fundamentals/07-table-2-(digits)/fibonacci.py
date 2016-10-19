


# Print out the Fibonacci Sequence


# Solution #1
a, b = 0, 1
for i in xrange(0,10):
    print a
    a, b = b, a+b




# # Solution #2
# def fib(a=1, b=1):
#     while True:
#         yield a
#         a, b = b, a + b
# from itertools import islice
# print list(islice(fib(), 10))
