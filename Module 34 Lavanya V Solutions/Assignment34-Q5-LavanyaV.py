# finding index of max(twice) the element in array-
# time complexity- O(n)- linear


def find_max(arr):
    bigNo = 0

    for i in range(len(arr)):
        if arr[i] > bigNo:
            bigNo = arr[i]
            bigNoInd = i
    if arr[bigNoInd - 1] * 2 == bigNo:
        return bigNoInd
    else:
        return -1


arrInp = [int(x) for x in (input("Enter the values ")).split(",")]

print(find_max((arrInp)))
