# using XOR- time complexity os O(n) and constant extra space result


def unique_noByXor(arr):
    result = 0
    countFor0 = 0
    for i in range(len(arr)):
        # xor is bitwise operation
        # eg: 4(100)^2(010)= 100(which is 6) like wise done for all nos and finally
        # unique no will be given
        # xor will return the unique- all duplicates will get cancelled
        result = result ^ arr[i]
        if arr[i] == 0:
            countFor0 += 1
    if result == 0:
        # if no duplciates also, 0 is returned . and if 0 is the unique no
        # in that case also 0 is returned. so to differentiate between them.
        if countFor0 == 1:
            return result
        else:
            "No duplicates"
    else:
        return result


inpNos = [1, 3, 4, 2, 1, 4, 3]
print(unique_noByXor(inpNos))
