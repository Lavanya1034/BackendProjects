# employee details
class Employee:
    def __init__(self, nam, sal, department):
        self.name = nam
        self.__salary = int(sal[1:])
        self.dept = department

    def show(self):
        print(f"Name:  {self.name} Salary: {self.__salary} Dept: {self.dept}")


# instance of class- object
name = "Steve Rogers"
dept = "IT"
salary = "$10000"

emp1 = Employee(name, salary, dept)
# cannot access salary from outside reference -as set to private- shown in
# next assignment

emp1.show()
