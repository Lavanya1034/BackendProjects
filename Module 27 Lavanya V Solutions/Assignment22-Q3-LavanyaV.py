# to calculate amount to be paid to author

playDuration = 120
subscribersCount = 5400567


def amounts(duration, subscribers):
    amount = 10  # alreday paid 10 ass initial payment
    if duration > 1000 and subscribers >= 1000000:
        amount = amount + 40
    elif duration > 500 and subscribers >= 500000:
        amount = amount + 30
    elif duration > 100 and subscribers >= 100000:
        amount = amount + 20

    return amount


print(f"The total payments to user is  {amounts(playDuration, subscribersCount)}$")
