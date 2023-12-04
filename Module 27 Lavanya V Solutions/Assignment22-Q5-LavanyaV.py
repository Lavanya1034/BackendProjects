# channel names more than 15 characters

Channels = [
    "Indie Folk Central",
    "RoadTravelledLess",
    "Netflix",
    "PlayStation",
    "RoadTravelledLess",
    "Python is Awesome",
    "JavaScript",
]


def channelNamesLength(channelNames):
    names = []
    for channel in channelNames:
        if len(channel) > 15:
            # checking if the channel name is not already in the array
            if not (channel in names):
                names.append(channel)
    if len(names) > 0:
        for nameList in names:
            print(nameList)


channelNamesLength(Channels)
