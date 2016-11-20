
# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?


# Option #1
def is_palindrome(s):
    if s == '':
        return true
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])


# Option #2
def iter_palendrome(s):
    for i in range(0, len(s) / 2):
        if s[i] != s[-(i + 1)]:
            return False



print iter_palendrome('abab')



#print is_palindrome('')
#>>> True
#print is_palindrome('abab')
#>>> False
#print is_palindrome('abba')
#>>> True