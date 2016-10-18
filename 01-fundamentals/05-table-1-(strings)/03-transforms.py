# http://www.tutorialspoint.com/python/python_strings.htm


dylan = "   Dylan Jorgensen   "

# White Space
print 'Removes all whitespace in string:', dylan.strip()
print 'Removes all leading whitespace in string:', dylan.lstrip()
print 'Removes all trailing whitespace in string:', dylan.rstrip()

print '\n'

# Cases
print 'Converts to titlecase:', dylan.title()
print 'Converts all upper to lower:', dylan.lower()
print 'Inverts all cases:', dylan.swapcase()
print 'Capitalizes first letter:', dylan.capitalize()

print '\n'

# Find and Replace
print 'find and replace', dylan.replace("sen", "son")

