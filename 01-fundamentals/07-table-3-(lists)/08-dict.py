
# Dictionaries are a series of key value pairs





# Curly Braces: {}
super_villains = {'Professor X' : 'Charles Xaviar', 'Wolverine' : 'Logan', 'DeadPool' : 'Wade Wilson'}


# List keys and values
print super_villains.keys()
print super_villains.values()
print super_villains.items()


# Select by keys and values
print super_villains['Wolverine']
print super_villains.get('Wolverine')


# Select by value
for alias_key, name_value in super_villains.items():
    if name_value == 'Logan':
        print alias_key


# Rename or add
super_villains['Professor X'] = 'Onsolot'
super_villains['Joker'] = 'Harley Quinn'


# Delete Entry
del super_villains['Wolverine']
print super_villains

