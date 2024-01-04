# defining a class


class Book:
    def __init__(self, title, fullName, price):
        self.title = title
        self.author = fullName
        self.price = price[1:]

    def view(self):
        print(
            f"Book Title : -> {self.title} Book Author : {self.author} Book Price : {self.price} $"
        )


# creating object and calling its method to view the details

bookName = input("Enter the book name ")
authorInp = input("Enter the author name ")
priceInp = input("Enter the price ")

book1 = Book(bookName, authorInp, priceInp)
book1.view()
