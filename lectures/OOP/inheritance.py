class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def about_me(self):
        print(f'I am {self.name} {self.last_name} and I am {self.age}')

    def info(self):
        print(f'Info about me')


class Student(Person):
    def __init__(self, university, name, last_name, age):
        super().__init__(name, last_name, age)
        self.university = university

    def about_me(self):
        print(f'Hi my name is {self.name}')

    def university_type(self):
        print(f'I am a student of {self.university} university')


# anna = Person('Anna', 'Back', 27)
# anna.about_me()

john = Student('John', '21', 2, 'LNU')

john.about_me()
john.university_type()
john.info()

# class Test:
#     pass
#
# foo = isinstance(john, Person)
# print(foo)
#
# bar = issubclass(Test, Person)
# print(bar)