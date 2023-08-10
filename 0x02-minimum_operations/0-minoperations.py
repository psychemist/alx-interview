#!/usr/bin/python3
"""Module minoperations"""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to result in
        exactly n H characters in the file

    Argument:
        n (int): number of characters of letter 'H' at the end of operations

    Return:
        operations (int): number of COPY ALL and PASTE operations necessary
        to transform one single character into n number of characters
    """
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
