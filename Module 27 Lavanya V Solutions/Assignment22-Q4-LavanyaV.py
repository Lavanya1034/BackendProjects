# to find all music channels
channels = ["Indie Folk", "RoadTravelled", "MusicStation", "Python", "JavaScript"]


def musicChannels(channelsName):
    result = ""
    for channel in channelsName:
        if (
            "music" in channel.lower()
            or "song" in channel.lower()
            or "folk" in channel.lower()
        ):
            result = result + ", " + channel if len(result) > 0 else result + channel

    return result


print(musicChannels(channels))
