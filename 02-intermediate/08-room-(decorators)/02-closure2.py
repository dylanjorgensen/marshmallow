# What I learned..
# - Our inner functions closes over and retains it's value
# - Functions are objects
# - We can returning a function as an object
# - Our passed argument becomes a global var to the inner function
# - What the inner func returns cascades out to the func return


# Example 1
def make_printer(word):
    def inner():
        return word + " L3"
    return inner()

print 'Example 1', make_printer("Hello")  # Returns: Hello L3


# Example 2
def large(word):
    def med():
        def small():
            return word + " L3"
    return med()

print 'Example 2', large("Hello")  # Returns: None