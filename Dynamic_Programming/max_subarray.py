def max_subrray_sum(num_list: list[int]) -> int:
    if not num_list:
        return 0
    dp = [0] * len(num_list)
    for i, num in enumerate(num_list):
        dp[i] = max(num, dp[i - 1] + num)
    return max(dp)
    
print(max_subrray_sum([]))