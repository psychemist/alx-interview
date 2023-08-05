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
    stack = [0]

    # Perform depth-first search to open boxes
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
