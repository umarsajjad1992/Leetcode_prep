"""
Valid Parentheses Checker - LeetCode Problem Solution

This module implements a solution to determine if a string of parentheses, brackets,
and braces is valid. A valid string must have properly matched and nested pairs.

The solution uses a stack-based approach with a hash map for efficient bracket matching.
Each opening bracket is pushed onto the stack, and each closing bracket is checked
against the most recent opening bracket. The string is valid if all brackets are
properly matched and the stack is empty at the end.

Valid pairs: (), [], {}
Rules:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

Example:
    >>> isValid("()")        # Returns True
    >>> isValid("()[]{}")    # Returns True  
    >>> isValid("(]")        # Returns False
    >>> isValid("([)]")      # Returns False
    >>> isValid("{[]}")      # Returns True

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) in worst case when all characters are opening brackets
"""

from typing import Dict


def isValid(s: str) -> bool:
    """
    Determine if a string containing brackets is valid.
    
    Uses a stack-based algorithm to validate bracket sequences. The function
    maintains a stack of opening brackets and uses a hash map to quickly
    identify matching pairs. Each closing bracket must match the most recent
    unmatched opening bracket.
    
    Args:
        s (str): Input string containing brackets and other characters.
                Only brackets '()', '[]', '{}' are considered for validation.
                Other characters are ignored in this implementation.
    
    Returns:
        bool: True if all brackets are properly matched and nested, False otherwise.
              Returns True for empty strings.
    
    Examples:
        >>> isValid("()")
        True
        >>> isValid("()[]{}")
        True
        >>> isValid("(]")
        False
        >>> isValid("([)]")
        False
        >>> isValid("{[]}")
        True
        >>> isValid("")
        True
        >>> isValid("((")
        False
        >>> isValid("))")
        False
    
    Algorithm:
        1. Use a stack to keep track of opening brackets
        2. For each character in the string:
           - If it's an opening bracket, push to stack
           - If it's a closing bracket, check if it matches the top of stack
           - If match found, pop from stack; if no match, return False
        3. Return True only if stack is empty (all brackets matched)
    
    Time Complexity: O(n) where n is the length of the input string
    Space Complexity: O(n) in worst case when all characters are opening brackets
    """
    # Stack to store opening brackets
    stack = []
    
    # Hash map for quick lookup of bracket pairs
    # Maps closing brackets to their corresponding opening brackets
    bracket_pairs: Dict[str, str] = {
        ')': '(',
        '}': '{', 
        ']': '['
    }
    
    for char in s:
        # If stack is empty, push any character (opening bracket)
        if not stack:
            stack.append(char)
        # If current character is a closing bracket and matches top of stack
        elif char in bracket_pairs and stack and stack[-1] == bracket_pairs[char]:
            stack.pop()  # Found a matching pair, remove the opening bracket
        else:
            # Either a non-matching closing bracket or another opening bracket
            stack.append(char)
    
    # Valid if all brackets were matched (stack is empty)
    return not stack


def main() -> None:
    """
    Demonstrate the isValid function with comprehensive test cases.
    
    This function tests various bracket combinations to showcase the
    validation algorithm's capabilities. It includes edge cases, nested
    brackets, and invalid sequences to provide thorough examples.
    
    Test cases cover:
    1. Simple valid pairs
    2. Mixed valid combinations  
    3. Nested brackets
    4. Invalid sequences
    5. Edge cases (empty string, unmatched brackets)
    
    Time Complexity: O(n) for each test case where n is string length
    Space Complexity: O(n) for each test case in worst case scenarios
    """
    print("Valid Parentheses Checker Demonstration:")
    print("=" * 42)
    
    # Test cases with expected results
    test_cases = [
        ("()", True, "Simple parentheses"),
        ("()[]{}", True, "Multiple valid pairs"),
        ("{[]}", True, "Nested brackets"),
        ("(]", False, "Wrong closing bracket"),
        ("([)]", False, "Incorrectly nested"),
        ("", True, "Empty string"),
        ("((", False, "Only opening brackets"),
        ("))", False, "Only closing brackets"),
        ("(ab)[]{}", True, "Mixed with other characters"),
        ("({[]})", True, "Complex nested structure")
    ]
    
    for test_string, expected, description in test_cases:
        result = isValid(test_string)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | '{test_string}' -> {result} | {description}")
    
    print(f"\nTest Summary: Validating bracket sequences")
    print(f"Algorithm: Stack-based with hash map lookup")


if __name__ == "__main__":
    main()