def longest_mount(num_list: list[int]) -> int:
    
    n = len(num_list)
    if n < 3:
        return 0


    count = 0
    for i in range(1, n - 1):
        if num_list[i - 1] < num_list[i] > num_list[i + 1]:
            l = r = i
            while l > 0 and num_list[l] > num_list[l-1]:
                l -= 1
            while r < n - 1 and num_list[r] > num_list[r+1]:
                r += 1
            count = max(count, r - l + 1)
    
    
    return count

print(longest_mount([2, 1, 4, 7, 3, 2, 1, 4, 6, 3, 2, 1, 0]))