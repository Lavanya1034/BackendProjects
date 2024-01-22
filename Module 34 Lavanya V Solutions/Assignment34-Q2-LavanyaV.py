# same prob as of assignment 1 using binary search
# with time complexity- O(logn)


def binary_search(inpArr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if target == inpArr[mid]:
            return mid
        elif target > inpArr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return low


arr = [int(x) for x in eval(input("Enter the values "))]
key = int(input("Enter the target key too be searched "))
start = 0
end = len(arr) - 1

print(binary_search(sorted(arr), key, start, end))
