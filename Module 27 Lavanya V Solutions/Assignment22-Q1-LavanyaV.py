# Longest running video

playTimes = [10.5, 45.67, 32.3, 9.28, 7.3, 55.67, 123.4, 11.2, 6.25, 3.9]


def longestRunning(plays):
    longest = 0
    for play in plays:
        if play > longest:
            longest = play
    return longest


print(f" Longest running video is : {longestRunning(playTimes)}")
