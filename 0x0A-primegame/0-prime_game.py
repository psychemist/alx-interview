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
    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def game_winner(n):
        """Return the winner of the game for a given n."""
        numbers = set(range(2, n + 1))
        current_player = "Maria"

        while True:
            # Find the smallest prime in the set
            prime = None
            for num in sorted(numbers):
                if is_prime(num):
                    prime = num
                    break
            
            # If no prime is found, the current player loses
            if prime is None:
                if current_player == "Maria":
                    return "Ben"
                else:
                    return "Maria"
            
            # Remove the prime and its multiples
            multiples = set(range(prime, n + 1, prime))
            numbers -= multiples
            
            # Switch player
            current_player = "Maria" if current_player == "Ben" else "Ben"

    # Play the game x times
    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        if game_winner(n) == "Maria":
            Maria_wins += 1
        else:
            Ben_wins += 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
