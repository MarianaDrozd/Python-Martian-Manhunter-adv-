class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print('Meow')

    def eat(self):
        print('Eating fish')


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print('Bark')

    def eat(self):
        print('Eating meat')


class CatDog(Cat, Dog):
    pass

barsik_rex = CatDog('CatDog')


barsik_rex.bark()
barsik_rex.meow()
barsik_rex.eat()
