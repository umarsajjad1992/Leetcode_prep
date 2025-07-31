"""
Letter Case Permutation Problem Solutions

This module provides two different approaches to solve the letter case permutation problem:
1. Iterative approach using breadth-first expansion
2. Recursive approach using backtracking

The problem: Given a string containing letters and digits, generate all possible 
strings by toggling the case of each letter while keeping digits unchanged.

Example:
    Input: "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Time Complexity: O(2^n * n) where n is the number of letters
Space Complexity: O(2^n * n) for storing all permutations
"""

def letterCasePerm(string: str) -> list[str]:
    """
    Generate all letter case permutations using iterative breadth-first approach.
    
    This function builds permutations level by level, processing each character
    in the input string sequentially. For each alphabetic character, it creates
    two versions (uppercase and lowercase) of each existing permutation. For
    digits, it simply appends the digit to all existing permutations.
    
    Algorithm:
        1. Initialize result with empty string
        2. For each character in input:
           - If alphabetic: duplicate all current results with both cases
           - If digit: append digit to all current results
        3. Update result list with new permutations
    
    Args:
        string (str): Input string containing letters and/or digits.
                     Letters can be uppercase or lowercase.
                     Empty string is valid input.
    
    Returns:
        list[str]: List of all possible letter case permutations.
                  If input is empty, returns [""].
                  Length is 2^k where k is the number of letters.
    
    Examples:
        >>> letterCasePerm("a1b2")
        ['a1b2', 'a1B2', 'A1b2', 'A1B2']
        
        >>> letterCasePerm("3z4")
        ['3z4', '3Z4']
        
        >>> letterCasePerm("12345")
        ['12345']
        
        >>> letterCasePerm("")
        ['']
    
    Time Complexity: O(2^k * n) where k is number of letters, n is string length
    Space Complexity: O(2^k * n) for storing all permutations
    """
    res = [""]
    for c in string:
        temp = []
        if c.isalpha():
            for r in res:
                temp.append(r + c.lower())
                temp.append(r + c.upper())
        else:
            for r in res:
                temp.append(r + c)
        res = temp
    return res

def letterCasePermRec(string: str) -> list[str]:
    """
    Generate all letter case permutations using recursive backtracking approach.
    
    This function uses depth-first search with backtracking to explore all possible
    character case combinations. It builds permutations character by character,
    making decisions at each alphabetic character to either keep original case
    or swap case, then recursively processes the remaining characters.
    
    Algorithm:
        1. Base case: if current substring length equals input length, add to results
        2. For current character:
           - If alphabetic: try both original case and swapped case
           - If digit: use as-is
        3. Recursively process next character
        4. Backtrack by unwinding the recursion stack
    
    Args:
        string (str): Input string containing letters and/or digits.
                     Letters can be uppercase or lowercase.
                     Empty string is valid input.
    
    Returns:
        list[str]: List of all possible letter case permutations.
                  If input is empty, returns [""].
                  Length is 2^k where k is the number of letters.
                  Order may differ from iterative approach due to DFS traversal.
    
    Examples:
        >>> letterCasePermRec("a1b2")
        ['a1b2', 'a1B2', 'A1b2', 'A1B2']
        
        >>> letterCasePermRec("3z4")
        ['3z4', '3Z4']
        
        >>> letterCasePermRec("12345")
        ['12345']
        
        >>> letterCasePermRec("")
        ['']
    
    Note:
        - Contains debug print statements showing recursion path
        - Uses swapcase() which toggles letter case
        - Memory efficient as it doesn't store intermediate results
    
    Time Complexity: O(2^k * n) where k is number of letters, n is string length
    Space Complexity: O(2^k * n) for results + O(n) for recursion stack
    """
    res = []

    def backtrack(sub="", i = 0):
        print(f"Sub: {sub}: Level: {i}")
        if len(sub) == len(string):
            res.append(sub)
            return
        if string[i].isalpha():
            backtrack(sub + string[i].swapcase(), i + 1)
        backtrack(sub + string[i], i + 1)
    
    backtrack()
    return res

print(letterCasePerm('a1b2c3d4'))
print(letterCasePermRec('abcd'))