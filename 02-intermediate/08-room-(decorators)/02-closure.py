# https://www.youtube.com/watch?v=swU3c34d2NQ


# # Example of how normal nested function looks & works
# def outer_func():
#     #string var looks like a "free var" to inner_func.
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     # outer_func() returns inner func like a var.
#     return inner_func()
#
# outer_func()



# Example of...
def outer_func():

    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func # *NOTICE the removed ()

var_func = outer_func()

print type(var_func) # Type is now function

var_func() # our new var acts like a func!!
