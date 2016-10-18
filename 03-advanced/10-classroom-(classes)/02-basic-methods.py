

class Animal(object):
    name = "none"
    legs = 4
    sound = "none"

    def set(self, name, legs, sound):
        self.name = name
        self.legs = legs
        self.sound = sound

def main():

    cat = Animal()
    cat.set("cat", 4, "meow")

    print cat.name, cat.legs, cat.sound



main()
