# https://www.youtube.com/watch?v=0tzSUyqVM8I&index=3&list=PL1A2CSdiySGIQZl3-v6o3iz-O5NO6roRl




class Animal(object):

    def __init__(self, name, legs, sound):
        self.name = name
        self.legs = legs
        self.sound = sound

def main():

    cat = Animal("cat", 4, "meow")

    print cat.name, cat.legs, cat.sound



main()

