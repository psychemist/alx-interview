#!/usr/bin/python3
"""validate_utf8 Module"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding
    """
    return all([byte <= 255 for byte in data])
