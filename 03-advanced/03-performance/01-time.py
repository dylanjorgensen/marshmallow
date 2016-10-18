
import time

def time_execution(code):
    start = time.clock()
    # eval() interprets a string as code.
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1


# String evaluate because of eval()
print time_execution('1 + 1')
print time_execution('34*100')

print time_execution('spin_loop(1000)')
print time_execution('spin_loop(10000000)')