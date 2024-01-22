# Linear search


def duplicate_nos(arr):
    dupArr = []
    for i in range(len(arr)):
        remArr = arr[i + 1 :]
        if arr[i] in remArr and not (arr[i] in dupArr):
            dupArr.append(str(arr[i]))
    if len(dupArr) < 1:
        return print("There are no duplicates")
    print(",".join(dupArr))


arrInp = [11, 21, 19, 34, 19, 23, 24, 22, 25, 22, 21, 11, 31]
duplicate_nos(arrInp)
