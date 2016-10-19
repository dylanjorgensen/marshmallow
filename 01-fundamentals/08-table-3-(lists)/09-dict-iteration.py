
example = {'dylan': 'happy',
           'matt': 'funny',
           'pig': 'food'}


# Iterate keys
for x in example.keys():  # Same as: for x in example:
    print 'keys:', x

# Iterate values
for x in example.values():
    print 'values:', x

# Iterate both
for x, y in example.items():
    print 'both:', x, y

