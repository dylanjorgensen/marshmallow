


nums = [1,2,3,4,5,6,7,8,9,10]

print 'No Change:', [i for i in nums]
print 'Multiply by 2:', [i*2 for i in nums]
print 'Filter for True', [i for i in nums if i%2 == 0]



# Normal for loop
my_list = []
for n in nums:
    my_list.append(n)
print my_list

# List comprehension
my_list = [n for n in nums]
print my_list

# List comprehension (squared)
my_list = [n*n for n in nums]
print my_list




# Normal loop (w/ if statement)
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print my_list

# List compression (if statement)
my_list = [n for n in nums if n%2 == 0]
print my_list



# Normal loop (w/ double for statement)
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print my_list

# List compression (double for statement)
my_list = [(letter, num) for Letter in 'abcd' for num in range(4)]
print my_list

