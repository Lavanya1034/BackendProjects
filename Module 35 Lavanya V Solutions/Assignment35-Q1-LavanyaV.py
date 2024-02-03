# returning letter occurs twice first


def string_check(str):
    arr = []
    for i in str:
        if i in arr:
            return i
        else:
            arr.append(i)


inpStr = input("Enter the string  ")
print(string_check(inpStr))
