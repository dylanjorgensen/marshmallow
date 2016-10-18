

class Person(object):
    name = "Joe"
    age = 40


def main():
    me = Person
    me.name = "dylan"
    me.age = "30"


    friend = Person
    friend.name = "Jill"
    friend.age = "25"

    print "Name " + me.name + " is " + me.age



main()