

# [start:end:stride]


# Generates a 11 digits list of squared numbers
list = [i ** 2 for i in range(1, 11)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print list


print list[2:9:2]  # [9, 25, 49, 81]

print list[::2]  # Skips every other one.


# Parsing backwards
print list[::-1] # A negative works through the list backwards
name = "Dylan Jorgensen"
print name[::-1]


