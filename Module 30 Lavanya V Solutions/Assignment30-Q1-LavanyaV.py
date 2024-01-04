# single Inheritance


# parent/base/super class
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print(f"Person name :  {self.name}")
        print(f"Person city =  {self.city}")


# student is child/derived/subclass class
class Student(Person):
    def __init__(self, name, city, section):
        Person.__init__(self, name, city)
        self.section = section

    def displayStudent(self):
        print(f"Student name :  {self.name}")
        print(f"Student city =  {self.city}")
        print(f"Student section =  {self.section}")


# object created

# object created only for person class- parent class

person1 = Person("Steve", "San Diego")
person1.display()

print("------------------------------------------")

# object created for child class- student class- which inherits parent class
# attributes also
StudentName = "Tony"
StudentCity = "New York"
StudentSection = "Mathematics"
student = Student(StudentName, StudentCity, StudentSection)
# method from student child class- which also displays the inheritted attributes
student.displayStudent()
