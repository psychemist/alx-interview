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
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
