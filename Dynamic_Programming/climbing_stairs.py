"""
Climbing Stairs Problem Solution

Find the number of distinct ways to climb n stairs where you can climb either 1 or 2 steps at a time.
Uses dynamic programming approach to efficiently solve the problem.

Example: n=4 → 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
"""

def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs.
    
    Args:
        n (int): Number of stairs to climb (non-negative integer)
        
    Returns:
        int: Number of distinct ways to reach the top
        
    Algorithm:
        1. Handle base cases: 0, 1, and 2 stairs
        2. Create a DP array to store results for each step
        3. For each step i, ways[i] = ways[i-1] + ways[i-2]
        4. This follows the Fibonacci sequence pattern
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> climb_stairs(4)
        5  # Five different ways to climb 4 stairs
        >>> climb_stairs(3)
        3  # Three different ways to climb 3 stairs
    """
    dp = [0]*(n+1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
         return 2
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(climb_stairs(4))