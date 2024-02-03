# maximum possible sum of ascending integers


def add(arr, l, r):
    if l <= r:
        sum = 0
        for i in range(l, r + 1):
            sum = sum + arr[i]
        return sum


def max_asc(arr):
    ascArr = []
    if len(arr) < 2:
        return arr[0]
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            left = right = i
            while right + 1 < len(arr) and arr[right] < arr[right + 1]:
                right = right + 1
            if right == len(arr) - 1:
                return add(arr, left, right)


inpArr = [int(x) for x in input("Enter the nos  ").split(",")]
# inpArr = [10, 20, 30, 5, 10, 50]
print(max_asc(inpArr))
