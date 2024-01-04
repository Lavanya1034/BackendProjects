# checking the given no is > or < or = to 7

# function to check whether the given no is > or < or = to 7


def compareWith7(no):
    if no > 7:
        return "UP"
    elif no < 7:
        return "DOWN"
    else:
        return "EQUAL"


t = int(input("Enter the no of test cases  "))

for i in range(t):
    n = int(input("Enter the no   "))
    print(compareWith7(n))
