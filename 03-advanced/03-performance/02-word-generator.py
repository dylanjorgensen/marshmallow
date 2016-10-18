

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


def make_string(p):
    S = ""
    for e in p:
        s = s + e
    return s



def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index


index10000 = make_big_index(10000)
time_execution('lookup')