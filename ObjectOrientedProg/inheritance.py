class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print('AW AW')

class Cat(Animal):
    def speak(self):
        print('Meow meow')

class Kalabaw(Animal):
    def speak(self):
        print('mowoooooooooooooooooooooooo')

dog = Dog('Robinson')
cat = Cat('Ming')
kalabaw = Kalabaw('San Pedro')

print(dog.name)
print(dog.is_alive)
cat.eat()
kalabaw.sleep()

kalabaw.speak()
cat.speak()