#!/usr/bin/python3
""" Prime Game algorithm module
"""


def isWinner(x, nums):
    """Determine winner of a turn-based gam einvlving primes
    Args:
        x (int): number of rounds
        nums (int): array of numbers
    Returns:
        (str): name of player that won the most rounds
    """
    # Using Sieve of Eratosthenes to precompute primes up to 10,000
    N = 10001
    sieve = [True] * N
    sieve[0], sieve[1] = False, False
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = False
    primes = [i for i in range(2, N) if sieve[i]]

    # Calculate cumulative count of primes up to each number
    prime_counts = [0] * N
    count = 0
    for i in range(2, N):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    # Determine winners for each game
    Maria_wins, Ben_wins = 0, 0
    for n in nums:
        if prime_counts[n] % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    # Return overall winner
    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
