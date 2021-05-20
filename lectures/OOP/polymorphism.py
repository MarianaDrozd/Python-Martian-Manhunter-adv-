class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print(f'I am a cat and my name is {self.name} and I am {self.age} years old')

    def make_sound(self):
        print(f'{self.name}: Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print(f'I am a dog and my name is {self.name} and I am {self.age} years old')

    def make_sound(self):
        print(f'{self.name}: Bark')


barsik = Cat('Barsik', 2)
rex = Dog('Rex', 3)

for animal in (barsik, rex):
    animal.make_sound()
    animal.about_me()
    animal.make_sound()

barsik.make_sound()
barsik.about_me()
barsik.make_sound()
rex.make_sound()
rex.about_me()
rex.make_sound()
