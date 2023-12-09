# longest play time for given dictionaries

videos = {
    "Tuple in Python": [13.0, 134.5, 89.3, 98.4],
    "Lists in Python": [72.0, 83.5, 90.3, 98.4],
    "Dictionary in Python": [41.0, 114.5, 62.3, 198.4],
}


def longestInDict(inpDict):
    result = []
    for key in inpDict:
        result.append(max(inpDict[key]))
    return ",".join(map(str, result))


print(longestInDict(videos))
