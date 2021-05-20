class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self._last_name = last_name
        self.__age = age

    def print_about_person(self):
        print(self.__age)


anna = Person('Anna', 'Back', 23)
print(anna.name)
print(anna._last_name)
print(anna.print_about_person())
