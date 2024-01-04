# dictionaries from tuples

videoTuple = ("Tuple in Python", [13.0, 134.5, 89.3, 98.4])

# method 1 - but this method works fine with length of tuple as 2


def changeToDic(inpTuple):
    newList = []
    # to use dict method, converting tuple for array of tuples
    newList.append(inpTuple)
    return dict(newList)


print(changeToDic(videoTuple))

# method 2 :

# when continuos input like
videoTuple1 = ("Tuple in Python", [13.0, 134.5, 89.3, 98.4], "data", [1, 2, 3])

dict1 = {}
for i in range(0, len(videoTuple1), 2):
    dict1[videoTuple1[i]] = videoTuple1[i + 1]
print(dict1)
