"""
FILE: max_profit.py

DESCRIPTION:
This script contains multiple implementations of functions to calculate the maximum profit 
that can be achieved from buying and selling a stock given a list of stock prices. Each 
function assumes that you can buy and sell the stock only once, and the goal is to maximize 
the profit.

FUNCTIONS:
1. max_stock_profit: A naive approach with O(n^2) time complexity.
2. max_stock_profit_greedy: A greedy algorithm with O(n) time complexity.
3. max_stock_profit_v2: An efficient version of the first attempt with O(n) time complexity.

EXAMPLE USAGE:
Input: [7, 1, 5, 3, 6, 4]
Output:
- max_stock_profit: 5
- max_stock_profit_greedy: 5
- max_stock_profit_v2: 5

TIME COMPLEXITY:
- max_stock_profit: O(n^2), due to nested iteration over the list.
- max_stock_profit_greedy: O(n), as it uses a single pass with two pointers.
- max_stock_profit_v2: O(n), as it iterates through the list once in reverse.
"""

# My first attempt (O(n^2) time complexity)
def max_stock_profit(prices: list[int]) -> int:
    profit = 0
    i = 0
    while i < len(prices) - 1:
        diff = max(prices[i+1:]) - prices[i]
        if  diff > profit:
            profit = diff
        i += 1
    return profit

# Greedy algorithm (O(n) time complexity)
def max_stock_profit_greedy(prices: list[int]) -> int:
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

# Efficient version of first attempt
def max_stock_profit_v2(prices: list[int]) -> int:
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