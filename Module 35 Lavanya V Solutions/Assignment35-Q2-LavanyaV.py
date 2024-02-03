# Finding best day to rob problem


def rob_day(security, time):
    arrOut = []
    if time == 0:  # if time is zero, all days are good to rob
        for i in range(len(security)):
            arrOut.append(i)
        return arrOut

    # # check whether days for time taken is present before and after and that too
    # # as mentioned in non-increase and non-decrease order
    # max_endPoint = abs((time * 3) - 1)
    if len(security) < 3:
        # there should be equal  no of elements before and after the pointer
        return "No sufficient data"

    for i in range(time, len(security) - time):
        leftCount = rightCount = 0
        if security[i - 1] >= security[i] <= security[i + 1]:
            left = right = i
            while (
                left > 0 and leftCount < time and security[left - 1] >= security[left]
            ):
                left -= 1
                leftCount += 1
            while (
                right + 1 < len(security)
                and rightCount < time
                and security[right] <= security[right + 1]
            ):
                right += 1
                rightCount += 1
            if leftCount == time and rightCount == time:
                arrOut.append(i)
    if len(arrOut) > 0:
        return arrOut
    else:
        return "No day is a good day to rob the bank"


inpArr = [int(x) for x in input("Enter the nos  ").split(",")]
timeTaken = int(input("Enter the time "))

print(rob_day(inpArr, timeTaken))
