#!/usr/bin/python3
"""Module 0-lockboxes contains a function that solves
the Lockboxes Algorithm problem
"""


def canUnlockAll(boxes):
    """Determines if all boxes in a box of boxes can be opened

    Argument:
        boxes (list): list of lists of integers

    Returns:
        True if all lists are reachable, else False
    """
    # Initialize chest of keys
    chest = [0]

    # Iterate over boxes and open first box
    for index, box in enumerate(boxes):
        if index == 0:
            chest.extend(box)
        # If key in key chest, open box and collect keys
        for key in box:
            if key in chest:
                chest.extend(boxes[key])

    # Eliminate spare keys
    keys = set(chest)

    print(chest)
    print(keys)

    # If all keys aare present, return true
    if len(keys) == len(boxes):
        return True
    return False
