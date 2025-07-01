def all_miss(num_list: list[int]) -> list[int]:

    num_set = set(num_list)
    miss_list = []

    for i in range(1, len(num_list) + 1):
        if i not in num_set:
            miss_list.append(i)
    
    return miss_list

print(all_miss([1,2,3,4,6,5,2,7]))