"""
Counting Bits Problem Solution

Count the number of 1's in the binary representation of each number from 0 to n using dynamic programming.
Uses bit manipulation properties to efficiently compute the count for each number.

Example: n=5 → [0,1,1,2,1,2] (binary: 0:0, 1:1, 2:10, 3:11, 4:100, 5:101)
"""

def counting_bits(n: int) -> list[int]:
    """
    Count the number of 1's in binary representation for each number from 0 to n.
    
    Args:
        n (int): Upper bound (inclusive) for counting bits
        
    Returns:
        list[int]: Array where result[i] = number of 1's in binary of i
        
    Algorithm:
        1. Create DP array where dp[i] = number of 1's in binary of i
        2. Track the most significant bit position (sig_bit)
        3. For each number i from 1 to n:
           - If i is a power of 2, update sig_bit to i
           - dp[i] = 1 + dp[i - sig_bit] (add 1 for current bit + count from remainder)
        4. This uses the property that removing the highest bit gives a smaller number
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> counting_bits(5)
        [0, 1, 1, 2, 1, 2]  # 0:0, 1:1, 2:10, 3:11, 4:100, 5:101
        >>> counting_bits(8)
        [0, 1, 1, 2, 1, 2, 2, 3, 1]  # Count of 1's in binary for 0-8
    """
    dp = [0] * (n+1)
    sig_bit = 1

    for i in range(1, n+1):
        if sig_bit*2 == i:
            sig_bit = i
        dp[i] = 1 + dp[i - sig_bit]

    return dp

counting_bits(8)