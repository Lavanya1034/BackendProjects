# longest play time for given dictionaries

videos = {
    "Tuple in Python": [13.0, 134.5, 89.3, 98.4],
    "Lists in Python": [72.0, 83.5, 90.3, 98.4],
    "Dictionary in Python": [41.0, 114.5, 62.3, 198.4],
}


def longestInDict(inpDict):
    result = []
    for key, value in inpDict.items():
        result.append(max(value))
    return ", ".join(map(str, result))


print(f"Method 1 using inbuilt method: {longestInDict(videos)}")

# time complexity for this method is O(n2)

# it can also be done using for loop to find the max but time complexity will again
# increase

# method 2:


def longestInDict(inpDict):
    result1 = []
    for key, value in inpDict.items():
        longestTime = 0
        for val in value:
            if val > longestTime:
                longestTime = val
        result1.append(longestTime)
    return ", ".join(map(str, result1))


print(f"Method 2 using for loop method: {longestInDict(videos)}")

# time complexity of this method 2 is more O(n3) as 2 for loops and 1 join-
# so method 1 is preferred with
# in built function
