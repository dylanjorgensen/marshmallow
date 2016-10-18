import datetime

today = datetime.date.today()
time = datetime.datetime.now().time()


# The goal of str is to print something readable,
print "\n"
print today
print time


# the goal repr is to print something you could cut and past back into python and use.
print "\n"
print repr(today)
print repr(time)

