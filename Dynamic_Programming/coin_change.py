def coinChange(coins: list[int], amount: int):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return dp[amount] if (dp[amount] != float('inf')) else -1

print(coinChange([1,2,5], 11))