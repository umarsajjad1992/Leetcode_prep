def miss_num(num_list: list[int]) -> int:

    num_list.sort()
    for i, num in enumerate(num_list):
        if i != num:
            return i
        
        if i == len(num_list) - 1:
            return i + 1

print(miss_num([0, 4, 2, 3, 1]))