# http://www.python-course.eu/lambda.php

# The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True.

# The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list.


fib = [0,1,1,2,3,5,8,13,21,34,55]

result = filter(lambda x: x % 2, fib)
print result # Returns all odd numbers

result = filter(lambda x: x % 2 == 0, fib)
print result # Returns all even numbers