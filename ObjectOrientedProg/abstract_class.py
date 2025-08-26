from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print('Car go brooooooom!!!')

    def stop(self):
        print('Car Stop!!!')

class Motor(Vehicle):

    def go(self):
        print('Motor go brooooooom!!!')

    def stop(self):
        print('Motor Stop!!!')

class Boat(Vehicle):
    def go(self):
        print('Boat go brooooooom!!!')
    def stop(self):
        print('Boat Stop!!!')

car = Car()
motor = Motor()
boat = Boat()

boat.go()