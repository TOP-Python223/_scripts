class Vehicle:
    definition = 'a mechanism that can move'

    def __init__(self, wheels: int | None):
        self.wheels = wheels

    def move(self):
        print(f'{self.__class__.__name__} is moving')


class Bicycle(Vehicle):
    pass


class Car(Vehicle):
    pass


class Train(Vehicle):
    definition = 'a mechanism that can move only within railroads'


class Helicopter(Vehicle):
    def move(self):
        print(f'{self.__class__.__name__} is flying')



v1 = Vehicle(None)
print(f'{v1.definition = }')

b1 = Bicycle(2)
print(f'{b1.definition = }')

c1 = Car(4)
print(f'{c1.definition = }')

t1 = Train(16)
print(f'{t1.definition = }')

h1 = Helicopter(0)
print(f'{h1.definition = }\n')

for v in (b1, c1, t1, h1):
    print(f'{v.__class__.__name__} has {v.wheels} wheels')
print()

v1.move()
b1.move()
c1.move()
t1.move()
h1.move()
