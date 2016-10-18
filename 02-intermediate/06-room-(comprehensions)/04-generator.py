# https://www.youtube.com/watch?v=3dt4OGnU5sM


nums = [1,2,3,4,5,6,7,8,9,10]

# This is how a normal generator function would look.
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
# for i in my_gen:
#     print i


# this is how a generator function can be shown with comprehension.
my_gen = (n*n for n in nums)
for i in my_gen:
    print i
