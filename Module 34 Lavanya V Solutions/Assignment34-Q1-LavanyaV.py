# Insert position - Linear search with time complexity O(n)


def linear_search(inpArr, target):
    for i in range(len(inpArr)):
        if not (target in inpArr):
            if target < inpArr[i]:
                return i
            elif i == len(inpArr) - 1:
                return i + 1
        if inpArr[i] == target:
            return i


arr = [int(x) for x in eval(input("Enter the values "))]

key = int(input("Enter the target key too be searched "))

print(linear_search(sorted(arr), key))
