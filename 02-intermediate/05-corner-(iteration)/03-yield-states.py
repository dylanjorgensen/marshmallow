# https://www.youtube.com/watch?v=mInegPmG65I

# Generator functions an "iterator object"
# Use function rather than separate class
# Generates the background code for next() & iter()
# uses a special statement called yield
# - yield saves the state of the generator and saves a resume point for when next() is called again



def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def primes(n = 1):
    while(True):
        # What is unique about generators is this "yield" statement
        # It will only return this number if "isprime" returns "True"
        # yield is similar to return but the next time the func is
        # called it will skip anything not satiable for use in a loop
        if isprime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print n