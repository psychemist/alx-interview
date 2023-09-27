#!/usr/bin/python3
""" 0-making_change module
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount
    Args:
        coins (list): values of the coins in your possession
        total (int): amount of chnage required
    Returns:
        change (int): fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    change = 0

    # sort coins list in descending order
    coins.sort(reverse=True)

    for coin in coins:
        while total >= coin:
            total -= coin
            change += 1

    if total == 0:
        return change
    return -1
