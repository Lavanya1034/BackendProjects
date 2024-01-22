# merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # create 2 empty arrays
    L = [0] * n1
    R = [0] * n2

    # filling these empty arrays
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # fixing indexes
    i = 0
    j = 0
    k = l

    # checking for nos and sorting
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1

        else:
            print(f"Inversion pair : {L[i], R[j]}")
            inversions.append([L[i], R[j]])
            arr[k] = R[j]
            j += 1

        k += 1

    # moving remaining elements
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        mid = l + (r - l) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


inpArr = [int(x) for x in input("Enter the nos ").split(",")]
n = len(inpArr)
inversions = []
merge_sort(inpArr, 0, n - 1)
print(inpArr)
print(f"inversion count is : {len(inversions)}")
