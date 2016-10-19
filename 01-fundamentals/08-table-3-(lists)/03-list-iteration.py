



# general for loop
for x in range(10):
    # print x
    pass

# Enumerate to iterate with index
for x, y in enumerate(range(10)):
    # print x, y
    pass



for x in range(20):
    if x not in [13,15,17]:
        # break  # Breaks out of loop
        continue # Skips single iteration
    else:
        print x
