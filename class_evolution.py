
class Proteus:
    def move(self):
        print(f'{self.__class__.__name__} moves')

    def eat(self):
        print(f'{self.__class__.__name__} eats')

    def reproduce(self):
        print(f'New {self.__class__.__name__} is born')
        return self.__class__()


class Fish(Proteus):
    def breath(self):
        print(f'{self.__class__.__name__} breathes')


class Reptile(Fish):
    def hide(self):
        print(f'{self.__class__.__name__} hides')


class Bird(Reptile):
    def fly(self):
        print(f'{self.__class__.__name__} flies')


class Mammals(Reptile):
    def care(self):
        print(f'{self.__class__.__name__} cares about others')


class Human(Mammals):
    def speak(self):
        print(f'{self.__class__.__name__} tells "Hello!"')


artem = Human()
artem.move()
artem.eat()
artem.hide()
artem.care()
artem.speak()

parrot = Bird()
parrot.eat()
parrot.fly()
