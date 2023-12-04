# videos played more than 2 hours

videosTimings = [110.5, 145.67, 32.3, 119.28, 7.3, 55.67, 123.4, 11.2, 226.25, 3.9]


# 2 hours means 120minutes
def aboveTwoHours(videos):
    count = 0
    for video in videos:
        if video > 120:
            count = count + 1
    return count


print(f"No of videos played above 2 hours are: {aboveTwoHours(videosTimings)}")
