# This only works in python 3.0


# Run with debugger then use alt-enter
# https://www.youtube.com/watch?v=J9SqqUM9uDs&index=30&list=PLQ176FUIyIUY5Ii58pzoZhS_3qIBL80nz


l_var = ["hi", "man"]
i_var = 456

def update_list(list):
    # type: (list) -> object
    list.append('hello')
    return list


print update_list(l_var)




def greet(name: str, age: int) -> str:
    print name
    print age
    print('Hello {0}, you are {1} years old'.format(name, age))


greet('dylan', 30)


def greeting(name: str) -> str:
    return 'Hello ' + name