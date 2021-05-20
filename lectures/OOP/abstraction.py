from abc import abstractmethod, ABC


class Greetings:

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError

    def say_goodbye(self):
        print('Goodbye')


class English(Greetings):
    def say_hello(self):
        print('Hello')


class Ukrainian(Greetings):
    def say_hello(self):
        print('Привіт')


en = English()
en.say_hello()
ukr = Ukrainian()
ukr.say_hello()


class GreetingABS(ABC):

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError


class Spain(GreetingABS):
    def say_hello(self):
        print('Hola')


sp = Spain()
sp.say_hello()

test = Greetings()
abc_test = GreetingABS()