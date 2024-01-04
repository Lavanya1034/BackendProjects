# Sum-product of no is natural no
# eg: 135 = (1+3+5)*(1*3*5) = 135


def natural_no_check(nos):
    sumOfNo = 0
    prodOfNo = 1
    for each in range(len(nos)):
        sumOfNo += int(nos[each])
        prodOfNo = prodOfNo * int(nos[each])
    sumProd = sumOfNo * prodOfNo
    if sumProd == int(nos):
        return "Yes"
    else:
        return "No"


t = int(input("enter the no of test cases  "))

for i in range(t):
    no = input("enter the no  ")
    print(natural_no_check(no))
