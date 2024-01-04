# calculation perimeter and area of rectangle


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
        print(f"The perimeter of rectangle is: {self.perimeter()}")
        print(f"The area of rectangle is:  {self.area()}")


# creating objects

length = 8
breadth = 6
rect1 = Rectangle(length, breadth)
rect1.display()
