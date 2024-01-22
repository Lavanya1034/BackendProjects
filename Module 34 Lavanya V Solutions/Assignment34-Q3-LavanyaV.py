# find the uniquee no without duplicates


# there are 2 methods - both with time complexity O(n^2) due to 2 for loops
# method 1:
def unique_no(arr):
    for i in range(len(arr)):
        i = 0  # sets the starting range from 0 always after pop
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                arr.pop(j)
                arr.pop(i)
                break
    if len(arr) > 0:
        return arr[0]
    else:
        return "No duplicates"


inpNos = [1, 3, 4, 6, 1, 4, 3]
print(f"The unique number without duplicates is {unique_no(inpNos)}")


# method 2:
# constant extra space "flag"


def unique_no(arr):
    for i in range(len(arr)):
        flag = True
        for j in range(len(arr)):
            if arr[i] == arr[j] and not (i == j):
                flag = False
        if flag:
            return arr[i]


inpNos = [1, 3, 4, 6, 1, 4, 3]
print(f"The unique number without duplicates is {unique_no(inpNos)}")
