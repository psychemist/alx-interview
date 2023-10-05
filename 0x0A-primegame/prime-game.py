#!/usr/bin/python3
""" Prime Game module
"""


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def remove_multiples(num, nums):
    """Remove multiples of num from nums."""
    return [x for x in nums if x % num != 0]


def play_game(n):
    """Return the winner of a game given a starting number n."""
    nums = list(range(1, n + 1))
    turn = "Maria"

    while True:
        prime_choices = [num for num in nums if is_prime(num)]
        # If no prime number is left.
        if not prime_choices:
            return "Maria" if turn == "Ben" else "Ben"
        # Get the first prime number as both play optimally.
        chosen_prime = prime_choices[0]
        nums = remove_multiples(chosen_prime, nums)
        turn = "Ben" if turn == "Maria" else "Maria"


def isWinner(x, nums):
    """Determine the winner over x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
