"""
Coin Change Problem Solution

Find the minimum number of coins needed to make up a given amount using dynamic programming.
Given an array of coin denominations, determine the fewest coins needed to make the target amount.

Example: coins=[1,2,5], amount=11 → 3 coins (5+5+1)
"""

def coinChange(coins: list[int], amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the given amount.
    
    Args:
        coins (list[int]): List of coin denominations available
        amount (int): Target amount to make change for
        
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
        
    Algorithm:
        1. Create DP array where dp[i] = minimum coins needed for amount i
        2. Initialize dp[0] = 0 (0 coins needed for amount 0)
        3. For each amount from 1 to target:
           - Try each coin denomination
           - If coin value <= current amount, update minimum
           - dp[i] = min(dp[i], 1 + dp[i - coin])
        4. Return dp[amount] if possible, otherwise -1
        
    Time: O(amount * len(coins)), Space: O(amount)
    
    Example:
        >>> coinChange([1,2,5], 11)
        3  # 5+5+1 = 11 using 3 coins
        >>> coinChange([2], 3)
        -1  # Impossible to make 3 with only coin 2
    """
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return int(dp[amount]) if (dp[amount] != float('inf')) else -1

print(coinChange([1,2,5], 11))