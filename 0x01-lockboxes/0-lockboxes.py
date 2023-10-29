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
    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a stack to perform depth-first search
    chest = [0]

    # Perform depth-first search to open boxes
    while chest:
        current_box = chest.pop()
        # Check if key in each box has been added to set
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                chest.append(key)

    # Check if all boxes are opened and return bool
    return len(opened_boxes) == len(boxes)
