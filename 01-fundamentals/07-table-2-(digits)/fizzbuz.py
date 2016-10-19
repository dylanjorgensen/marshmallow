


# If the number is dividable by 3, print "Fizz"
# If the number is dividable by 5, print "Buzz"
# If the number is dividable by 3, print "FizzBuzz"


# Solution #1
for count in xrange(1,101):
    if count % 5 == 0 and count % 3 == 0:
        print "FizzBuzz"
    elif count % 3 == 0:
        print "Fizz"
    elif count % 5 == 0:
        print "Buzz"
    else:
        print count



# Solution #2
# count = 0
# while count < 101:
#     if count % 5 == 0 and count % 3 == 0:
#         print "FizzBuzz"
#     elif count % 3 == 0:
#         print "Fizz"
#     elif count % 5 == 0:
#         print "Buzz"
#     else:
#         print count
#     count = count + 1