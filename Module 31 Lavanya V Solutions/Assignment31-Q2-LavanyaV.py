# average weight of class

# method 1 considerign dynamic input length


def avgWeight(arr):
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    return round(avg, 6)  # rounds to exactly 6 decimal places


arrInp = [int(x) for x in input("enter the weights of class  ").split()]
print(avgWeight(arrInp))

# --------------------------------------------------------------------------------
# method 2

# considering only 10 students in class as given in question - so length is 10


# def avgWeight(inp):
#     sum = 0
#     for i in range(10):
#         sum += int(inp[i])
#     avg = sum / 10  # here it is hardcoded as 10 max students as per question- but
#     # method 1 is preferable
#     return round(avg, 6)  # rounds to exactly 6 decimal places


# inp = input("Enter the weights of students  ").split()
# print(avgWeight(inp))
