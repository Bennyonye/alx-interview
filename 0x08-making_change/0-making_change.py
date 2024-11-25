#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.
    
    Returns:
        int: Minimum number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    # Sort coins in descending order for the greedy approach
    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total == 0:
            break
        # Use as many of this coin as possible
        count = total // coin
        num_coins += count
        total -= count * coin
    
    # If there's any amount left, it means the total can't be formed
    return num_coins if total == 0 else -1
