def permutations(num_list: list[int]) -> list[list[int]]:
    res = []
    def backtracking(start, end = len(num_list)):
        if start == end:
            res.append(num_list[:])
        for i in range(start, end):
            num_list[start], num_list[i] = num_list[i], num_list[start]
            backtracking(start+1)
            num_list[start], num_list[i] = num_list[i], num_list[start]
    
    backtracking(0)
    return res




print(permutations([1, 2, 3]))
        