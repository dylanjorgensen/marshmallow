

var_list_1 = [3, 1, 4, 2, 5]  #Creates an empty new list
var_list_2 = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
var_list_nested = [var_list_1, var_list_2] # Nested lists


# Length
print len(var_list_1)


# Sorting
var_list_1.sort()
print var_list_1
print sorted([9, 7, 5, 6, 8])

# List Slicing
print(var_list_2[1:3])


# Inserting
var_list_nested.insert(2, "hello")
print var_list_nested

# Apending
var_list_nested.append("Whaz up")
print var_list_nested


# Removing L1
var_list_nested.remove("hello")
print var_list_nested

# Removing L2 i in var_list_nested[var_list_1]:
for i in var_list_nested:
    try:
        i.remove('Tomatoes')
    except ValueError:
        pass
    else:
        break  # Value was found and removed
else:
    raise ValueError("'Tomatoes' not in nested list")
print var_list_nested

