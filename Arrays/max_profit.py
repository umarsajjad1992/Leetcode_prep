"""
Maximum Stock Profit Problem

Calculate maximum profit from buying and selling stock once.
Three implementations: O(n²) naive, O(n) greedy two-pointer, O(n) reverse iteration.
Example: [7, 1, 5, 3, 6, 4] → profit = 5 (buy at 1, sell at 6)
"""

def max_stock_profit(prices: list[int]) -> int:
    """
    Calculate max profit using naive approach.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit possible
        
    Algorithm:
        For each day, find maximum price in remaining days and calculate profit.
        Keep track of maximum profit found.
        
    Time: O(n²), Space: O(1)
    
    Example:
        >>> max_stock_profit([7, 1, 5, 3, 6, 4])
        5  # Buy at 1, sell at 6
    """
    profit = 0
    i = 0
    while i < len(prices) - 1:
        diff = max(prices[i+1:]) - prices[i]
        if  diff > profit:
            profit = diff
        i += 1
    return profit

def max_stock_profit_greedy(prices: list[int]) -> int:
    """
    Calculate max profit using greedy two-pointer approach.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit possible
        
    Algorithm:
        Use two pointers (left=buy, right=sell). Move right pointer forward.
        If profitable, update max profit. If not, move left to right (new buy day).
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> max_stock_profit_greedy([7, 1, 5, 3, 6, 4])
        5  # Buy at 1, sell at 6
    """
    maxProf = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxProf = max(maxProf, profit)
        else:
            l = r  
        r += 1
    return maxProf

def max_stock_profit_v2(prices: list[int]) -> int:
    """
    Calculate max profit using reverse iteration approach.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit possible
        
    Algorithm:
        Iterate prices in reverse. Track maximum price seen so far (future max).
        For each price, calculate profit as (future max - current price).
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> max_stock_profit_v2([7, 1, 5, 3, 6, 4])
        5  # Buy at 1, sell at 6
    """
    maxPrice = float('-inf')
    profit = 0
    for price in prices[::-1]:
        if price > maxPrice:
            maxPrice = price
        profit = max(profit, maxPrice - price)
    
    return profit

print(max_stock_profit([7, 6, 5, 4, 1, 15]))
print(max_stock_profit_greedy([7, 1, 5, 3, 6, 4]))
print(max_stock_profit_v2([7, 1, 5, 3, 6, 4]))