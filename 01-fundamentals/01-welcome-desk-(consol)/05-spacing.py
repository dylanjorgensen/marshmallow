

# "Return", one tab in will return a squared list (correct)
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([2,3,4,5])

print my_nums # [4, 9, 16, 25]



# "Return", two tabs in will return a single scalar squared (incorrect)
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
        return result

my_nums = square_numbers([2,3,4,5])

print my_nums # [4]

