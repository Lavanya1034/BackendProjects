# sorting-descending

video = ["List in Python", [34.5, 19.2, 381.3, 56.2, 16.1]]


def sorting(inpVideo):
    inpVideo[1].sort(reverse=True)
    return inpVideo[1]


print(sorting(video))