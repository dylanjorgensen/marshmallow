# http://anandology.com/python-practice-book/iterators.html

# The __iter__ method is what makes an object iterable. Behind the scenes, the iter function calls __iter__ method on the given object.

# The return value of __iter__ is an iterator. It should have a next method and raise StopIteration when there are no more elements.






# Iterators are implemented as classes. Here is an iterator that works like built-in xrange function.

# To make a class iterable requires both...
#     def __iter__(self):
#     def __next__(self):

class YRange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()



y = YRange(3)

print y.next()
print y.next()




# Many built-in functions accept iterators as arguments.
list(YRange(5)) # [0, 1, 2, 3, 4]
sum(YRange(5)) # 10