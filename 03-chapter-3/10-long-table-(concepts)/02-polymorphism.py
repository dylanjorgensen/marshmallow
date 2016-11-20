


class Pet(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("subclass must implement abstract method")

class Cat(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def talk(self):
        return "meow"


class Dog(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def talk(self):
        return "bark"



def main():

    # List assumes they are pet objects because they are instances of sub classes
    pets = [Cat("Marbles", 4), Dog("Banyon", 10)]

    for pet in pets:
        # Notice pet.talk() is a function
        print "Name:", pet.name, "Age:", pet.age, "Talk: ", pet.talk()

main()
