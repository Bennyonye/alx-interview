#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generates a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def is_winner(x, nums):
    """Returns the name of the player who won the most rounds."""
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        remaining_numbers = set(range(1, n + 1))
        
        # Simulate the game
        turn = 'Maria'  # Maria always goes first
        while primes:
            prime = primes.pop(0)
            # Remove the prime and its multiples from the remaining numbers
            to_remove = set(range(prime, n + 1, prime))
            remaining_numbers -= to_remove
            
            # Check if the opponent can make a move
            if not remaining_numbers:
                break
            
            # Swap turns
            if turn == 'Maria':
                turn = 'Ben'
            else:
                turn = 'Maria'
        
        # Count the winner for this round
        if turn == 'Maria':
            ben_wins += 1
        else:
            maria_wins += 1

    # Return the winner with the most wins
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
