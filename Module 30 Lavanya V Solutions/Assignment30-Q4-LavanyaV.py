# Polymorphism = method overloading - based on parameters


class Calculate:
    def add(self, a=0, b=0, c=0):
        return a + b + c


set1 = Calculate()
print(f"Sum Value: {set1.add()}")
print(f"Sum Value: {set1.add(3,3,3)}")
print(f"Sum Value: {set1.add(5,5)}")
