def two_sum(num_list: list[int], target) -> list[int]:

    hash_map = {}

    for i, num in enumerate(num_list):
        temp = target - num
        if temp not in hash_map.keys():
            hash_map[num] = i
        else:
            return [hash_map[temp], i]
        
def two_sum_v2(num_list: list[int], target) -> list[int]:

    hash_map = {}

    for ind, num in enumerate(num_list):
        diff = target - num
        if diff in hash_map.keys():
            return [hash_map[diff], ind]
        hash_map[num] = ind
            


print(two_sum_v2([2, 7, 11, 15], 2))