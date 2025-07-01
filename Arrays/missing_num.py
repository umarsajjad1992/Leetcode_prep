# Good Solution but Slow
def miss_num(num_list: list[int]) -> int:

    num_list.sort()
    for i, num in enumerate(num_list):
        if i != num:
            return i
        
        if i == len(num_list) - 1:
            return i + 1

def fast_miss_num(num_list: list[int]) -> int:
    return (sum(range(len(num_list) + 1)) - sum(num_list))

print(fast_miss_num([0, 4, 5, 3, 1]))