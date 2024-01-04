## employee details
class Employee:
    def __init__(self, nam, sal, department):
        self.name = nam
        self.__salary = sal[1:]
        self.dept = department

    def show(self):
        print(f"Name:  {self.name} Salary: {self.__salary} Dept: {self.dept}")


# instance of class- object
name = "Steve Rogers"
dept = "IT"
salary = "$10000"

emp2 = Employee(name, salary, dept)
emp2.show()
emp2.name = "Tony"
emp2.show()
print(emp2.__salary)  # --- throws errror
# private attributes can be accessed only through class methods
