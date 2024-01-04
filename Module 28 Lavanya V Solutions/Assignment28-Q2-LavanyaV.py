# finding longest play time

# method 1 using max inbuilt method

videoTuple = ("Tuple in Python", [13.0, 134.5, 89.3, 98.4])


def longestPlayTime(tupleInp):
    return max(tupleInp[1])


print(f"Method 1 using inbuilt max method: {longestPlayTime(videoTuple)}")

# --------------------------------------------------------------------------

# method 2 using for loop


def longestPlayTime(tupleInp):
    max = 0
    for each in tupleInp[1]:
        if each > max:
            max = each
    return max


print(f"Method 2 using for loop method: {longestPlayTime(videoTuple)}")
