# largest positive integer


def largest_positive(arr):
    posNo = 0

    for i in arr:
        if i > 0 and -i in arr and i > posNo:
            posNo = i
    if (
        posNo == 0
    ):  # because mentioned no zero in array, so if it has zero, then it means
        # no greater positive integer
        return -1
    else:
        return posNo


inpArr = [int(x) for x in input("Enter the nos  ").split(",")]
print(largest_positive(inpArr))
