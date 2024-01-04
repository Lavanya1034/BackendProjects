# inheritance - for rectangle perimeter and area calculation


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"The length of rectangle is:  {self.length}")
        print(f"The width of rectangle is:  {self.width}")
        print(f"The perimeter of rectangle is:  {self.perimeter()}")
        print(f"The area of rectangle is:  {self.area()}")


# child class


class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        print(f"the volume of my_cuboid is:  {self.length * self.width * self.height}")


# creating object

rec1 = Cuboid(7, 5, 2)
rec1.display()
print("----------------------------------")
rec1.volume()
