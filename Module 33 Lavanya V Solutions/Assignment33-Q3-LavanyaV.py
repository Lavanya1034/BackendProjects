# bubble sort
def bubble_srt(arr):
    swapCount = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapCount += 1
                print(arr)
    return swapCount


inpArr = [int(x) for x in input("Enter the nos ").split(",")]

print(f"The no of swap count is : {bubble_srt(inpArr)}")
