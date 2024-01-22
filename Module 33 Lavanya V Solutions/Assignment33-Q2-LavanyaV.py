# binary search
def find_position(arr, key, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l #gives the insert position finally
    ################################################################
    # another method -inserting using linear search

    # # if key is not present, key is inserted at right position
    # if not (key in arr):
    #     for i in range(len(arr)):
    #         if key < arr[i]:  # to find the position and insert
    #             arr.insert(i, key)
    #             print(
    #                 f"As {key} is not present in the array but can be inserted at index {i} to make the array sorted."
    #             )
    #             return i  # returning that index
    #     arr.append(key)  # if it is largest no,appended at last
    #     print(
    #         f"As {key} is not present in the array but can be inserted at index {i+1} to make the array sorted."
    #     )
    #     return len(arr) - 1  # that index is returned
    ###############################################################
    # if key is present, binary search is done


inpArr = [int(x) for x in input("Enter the nos ").split(",")]
n = len(inpArr)
keyInp = int(input("Enter the target key to find "))
print(
    f"The position of the target no {keyInp} is : {find_position(inpArr, keyInp, 0, n - 1)}"
)
print(f"The final array is : {inpArr}")
