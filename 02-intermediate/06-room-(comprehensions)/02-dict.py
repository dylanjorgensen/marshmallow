

# Normal loop to make a dict out of lists
names = ['Bruce', 'C1ark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Super_man', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print my_dict

my_dict = {name: hero for name, hero in zip (names, heros)}
print my_dict

my_dict = {name: hero for name, hero in zip (names, heros) if name != 'Peter'}
print my_dict