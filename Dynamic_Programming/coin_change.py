def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount+1)
    return 0