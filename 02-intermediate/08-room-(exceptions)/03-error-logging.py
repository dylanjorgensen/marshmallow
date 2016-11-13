


def test(x,y):
    if x + y == 10:
        print "It's 10"
    else:
        raise NotImplementedError("subclass must implement abstract method")


test(5,5)