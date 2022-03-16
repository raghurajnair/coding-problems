def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0

    for idx in range(len(coins)):
        if coins[idx] > currentChange + 1:
            return currentChange + 1
        else:
            currentChange += coins[idx]

    return currentChange + 1