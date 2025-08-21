class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stopped the {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("Honda Civic", 2006, "Red", "True")
car2 = Car("Wigo", 2015, "Orange", False)

car1.drive()
car2.drive()
print()
car1.stop()
print()
car1.describe()
car2.describe()