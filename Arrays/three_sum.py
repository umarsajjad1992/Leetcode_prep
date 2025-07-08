def threeSum(num_list: list[int]) -> list[list[int]]:
    num_list.sort()

    ret = set()
    for ind, val in enumerate(num_list):

        i = val
        l, r = ind + 1, len(num_list) - 1

        while l < r:

            j, k = num_list[l], num_list[r]
            current_sum = i + j + k
            
            if  current_sum == 0:
                ret.add((i, j, k))
                break
            elif current_sum > 0:
                r -= 1
            else:
                l += 1
    return [list(item) for item in ret]

def threeSum_v2(num_list: list[int]) -> list[list[int]]:
    num_list.sort()
    ret = []
    n = len(num_list)
    for ind, val in enumerate(num_list):
        if ind > 0 and val == num_list[ind - 1]:
            continue
        i = val
        l, r = ind + 1, n - 1
        while l < r:
            j, k = num_list[l], num_list[r]
            currentSum = i + j + k
            if currentSum == 0:
                ret.append([i, j, k])
                while l < r and j == num_list[l + 1]:
                    l += 1
                l += 1
            elif currentSum < 0:
                l += 1
            else:
                r -= 1
    return ret

print(threeSum_v2([-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3, 5, -6, 2, 3]))
# [-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3]