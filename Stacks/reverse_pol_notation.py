"""
Reverse Polish Notation Evaluator - LeetCode Problem Solution

This module implements a solution to evaluate arithmetic expressions in Reverse Polish Notation (RPN).
RPN is a mathematical notation where operators follow their operands, eliminating the need for parentheses.

The solution uses a stack-based approach where operands are pushed onto the stack and operators
pop their required operands, perform the calculation, and push the result back onto the stack.
The final result is the single value remaining on the stack.

Supported operators: +, -, *, /
Rules:
1. Operands are pushed onto the stack
2. When an operator is encountered, it pops the required number of operands
3. The operation is performed and the result is pushed back
4. The final answer is the last remaining value on the stack

Example:
    For expression ["2", "1", "+", "3", "*"] -> returns 9 (equivalent to (2+1)*3)
    For expression ["4", "13", "5", "/", "+"] -> returns 6 (equivalent to 4+(13/5))
    For expression ["10", "6", "9", "3", "+"] -> returns [10, 6, 12] then continues...

Time Complexity: O(n) where n is the number of tokens in the expression
Space Complexity: O(n) in worst case when all tokens are operands
"""

from typing import List, Union


def reverse_notation(tokens: List[str]) -> float:
    """
    Evaluate an arithmetic expression in Reverse Polish Notation.
    
    Uses a stack-based algorithm to process RPN expressions. The function
    maintains a stack where operands are stored as numbers and operators
    consume operands from the stack to perform calculations. Each operator
    pops the required operands, performs the operation, and pushes the result back.
    
    Args:
        tokens (List[str]): List of tokens representing the RPN expression.
                           Contains string representations of numbers and operators.
                           Operators supported: '+', '-', '*', '/'
    
    Returns:
        float: The final result of evaluating the RPN expression.
               Returns the single value remaining on the stack after all operations.
    
    Examples:
        >>> # Expression: ["2", "1", "+", "3", "*"]
        >>> # Returns 9.0 (equivalent to (2+1)*3)
        
        >>> # Expression: ["4", "13", "5", "/", "+"]  
        >>> # Returns 6.0 (equivalent to 4+(13/5))
        
        >>> # Expression: ["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"]
        >>> # Returns 5.0 (complex nested operations)
    
    Algorithm:
        1. Initialize an empty stack
        2. For each token in the expression:
           - If token is a number, push it onto the stack as integer
           - If token is an operator, pop two operands (right then left)
           - Perform the operation: left operator right
           - Push the result back onto the stack
        3. Return the final value on the stack
    
    Note:
        Division is performed as integer division (truncated towards zero)
        as per LeetCode problem specification.
    
    Time Complexity: O(n) where n is the number of tokens in the expression
    Space Complexity: O(n) in worst case when all tokens are operands
    """
    # Stack to store operands and intermediate results
    stack = []
    
    for token in tokens:
        # If token is not an operator, it's an operand
        if token not in '+-*/':
            stack.append(int(token))
        else:
            # Pop two operands (order matters: right operand first, then left)
            right_operand = stack.pop()
            left_operand = stack.pop()
            
            # Perform the operation based on the operator
            if token == '+':
                result = left_operand + right_operand
            elif token == '-':
                result = left_operand - right_operand
            elif token == '*':
                result = left_operand * right_operand
            else:  # token == '/'
                # Integer division truncated towards zero
                result = int(float(left_operand) / right_operand)
            
            # Push the result back onto the stack
            stack.append(result)
            print(f"Stack after {left_operand} {token} {right_operand}: {stack}")
    
    # The final result is the only remaining value on the stack
    return float(stack.pop())


def main():
    """
    Demonstrate the reverse_notation function with comprehensive test cases.
    
    This function tests various RPN expressions to showcase the
    evaluation algorithm's capabilities. It includes simple operations,
    complex nested expressions, and edge cases to provide thorough examples.
    
    Creates test cases covering basic arithmetic, division with truncation,
    and complex multi-step expressions. For each test, it shows the input
    expression and the computed result.
    """
    # Test cases with different RPN expressions
    test_expressions = [
        (["2", "1", "+", "3", "*"], 9.0, "Simple expression: (2+1)*3"),
        (["4", "13", "5", "/", "+"], 6.0, "Division with addition: 4+(13/5)"),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22.0, "Complex nested expression"),
        (["3", "11", "+", "15", "-"], -1.0, "Addition then subtraction"),
        (["18", "6", "/", "3", "*"], 9.0, "Division then multiplication"),
        (["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"], 5.0, "Very complex expression")
    ]
    
    print("Reverse Polish Notation Evaluator Demonstration:")
    print("=" * 52)
    
    for expression, expected, description in test_expressions:
        print(f"\nEvaluating: {expression}")
        print(f"Description: {description}")
        result = reverse_notation(expression.copy())  # Use copy to avoid modifying original
        status = "✓ PASS" if abs(result - expected) < 0.001 else "✗ FAIL"
        print(f"{status} | Result: {result} | Expected: {expected}")
        print("-" * 50)
    
    print(f"\nTest Summary: Evaluating RPN expressions")
    print(f"Algorithm: Stack-based with operator precedence handling")


if __name__ == "__main__":
    main()