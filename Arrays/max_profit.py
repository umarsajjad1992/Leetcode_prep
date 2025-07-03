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