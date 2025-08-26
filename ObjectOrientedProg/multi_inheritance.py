#multiple inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating Yum Yum")

    def sleep(self):
        print(f"{self.name} is sleeping ZZZZZZZZZZZZZZZZZZZZZZZZ")
    
class Prey(Animal):
    def flee(self):
        print(f"{self.name} Run!!!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} enters Hunter mode!")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit('Bugs')
hawk = Hawk('Raven')
fish = Fish('Dory')

fish.eat()
hawk.hunt()
rabbit.sleep()