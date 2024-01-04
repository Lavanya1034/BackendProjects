# even no of digits in python

# function to find even digit nos


def even_digit(no):
    outputArr = []
    for each in no:
        if len(each) % 2 == 0:
            outputArr.append(each)
    return " ".join(outputArr)


t = int(input("Enter the no of test cases  "))

for i in range(t):
    n = [i for i in input("enter the no of elements  ").split()]
    print(even_digit(n))
