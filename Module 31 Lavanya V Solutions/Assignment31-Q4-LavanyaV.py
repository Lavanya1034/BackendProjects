# sum of its digits


def natural_no_check(nos):
    sumOfNo = 0
    for each in range(len(nos)):
        sumOfNo += int(nos[each])
    return sumOfNo


t = int(input("enter the no of test cases  "))

for i in range(t):
    no = input("enter the no  ")
    print(natural_no_check(no))
