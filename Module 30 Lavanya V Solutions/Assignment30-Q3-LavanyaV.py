# polymorphism method- method overriding


class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def max_speed(self):
        print("Vehicle max speed is 150")

    def gears(self):
        print("Vehicle have 6 gear")

    def show(self):
        print(f"{self.name} {self.color} {self.price}")


# sub classes


class Car(Vehicle):
    def max_speed(self):
        print("Car max speed is 240")

    def gears(self):
        print("Car change 7 gear")


class Bus(Vehicle):
    def max_speed(self):
        print("Bus max speed is 200")

    def gears(self):
        print("Bus change 8 gear")


# creating object

car1 = Car("BMW", "Red", "20000")
car1.show()
car1.max_speed()
car1.gears()

print("---------------------------------------")

bus1 = Bus("Tavera x1", "white", "75000")
bus1.show()
bus1.max_speed()
bus1.gears()
