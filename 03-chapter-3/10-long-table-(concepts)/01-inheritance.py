


class Pet(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)



def main():

    ourPet = Pet("pet", 1)
    print "is ourPet at Pet?" + str(isinstance(ourPet, Pet))  # True
    print "is ourPet at Cat?" + str(isinstance(ourPet, Cat))  # False


    ourCat = Cat("marbles", 6)

    print "is ourCat at Pet?" + str(isinstance(ourCat, Pet))
    print "is ourCat at Cat?" + str(isinstance(ourCat, Cat))



main()