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
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
