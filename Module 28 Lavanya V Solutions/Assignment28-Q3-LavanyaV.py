# dictionaries from tuples

videoTuple = ("Tuple in Python", [13.0, 134.5, 89.3, 98.4])


def changeToDic(inpTuple):
    newList = []
    # to use dict method, converting tuple for array of tuples
    newList.append(inpTuple)
    return dict(newList)


print(changeToDic(videoTuple))
