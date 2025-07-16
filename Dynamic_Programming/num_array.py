"""
Range Sum Query Problem Solutions

Implement a data structure that supports efficient range sum queries on an array.
Two different approaches: naive summation and prefix sum (cumulative sum) optimization.

Example: nums=[-2,0,3,-5,2,-1], sumRange(2,5) → -1 (sum of [3,-5,2,-1])
"""

class NumArray(object):
    """
    Range sum query implementation using naive approach.
    
    This implementation calculates the sum by iterating through the range
    for each query, resulting in O(n) time complexity per query.
    """
    
    def __init__(self, nums) -> None:
        """
        Initialize the NumArray with the given array.
        
        Args:
            nums (list[int]): Input array of integers
            
        Time: O(1), Space: O(n)
        """
        self.nums = nums
    
    def sumRange(self, left, right):
        """
        Calculate sum of elements between indices left and right (inclusive).
        
        Args:
            left (int): Left boundary index (inclusive)
            right (int): Right boundary index (inclusive)
            
        Returns:
            int: Sum of elements from left to right
            
        Time: O(n), Space: O(1)
        
        Example:
            >>> obj = NumArray([-2, 0, 3, -5, 2, -1])
            >>> obj.sumRange(2, 5)
            -1  # Sum of [3, -5, 2, -1]
        """
        return sum(self.nums[left:right+1])
    
class NumArrayV2(object):
    """
    Range sum query implementation using prefix sum optimization.
    
    This implementation precomputes cumulative sums to answer range queries
    in O(1) time at the cost of O(n) preprocessing time and space.
    """
    
    def __init__(self, nums) -> None:
        """
        Initialize the NumArrayV2 with prefix sum array.
        
        Args:
            nums (list[int]): Input array of integers
            
        Algorithm:
            1. Create prefix sum array starting with [0]
            2. For each element, add it to the previous cumulative sum
            3. acc_nums[i] = sum of elements from index 0 to i-1
            
        Time: O(n), Space: O(n)
        """
        self.acc_nums = [0]

        for num in nums:
            self.acc_nums.append(self.acc_nums[-1] + num)
        
    def sumRange(self, left, right):
        """
        Calculate sum of elements between indices left and right (inclusive).
        
        Args:
            left (int): Left boundary index (inclusive)
            right (int): Right boundary index (inclusive)
            
        Returns:
            int: Sum of elements from left to right
            
        Algorithm:
            Uses prefix sum difference: sum(left, right) = prefix[right+1] - prefix[left]
            
        Time: O(1), Space: O(1)
        
        Example:
            >>> obj = NumArrayV2([-2, 0, 3, -5, 2, -1])
            >>> obj.sumRange(2, 5)
            -1  # Sum of [3, -5, 2, -1] using prefix sum
        """
        return self.acc_nums[right+1] - self.acc_nums[left]

obj1 = NumArray([-2, 0, 3, -5, 2, -1])
obj2 = NumArrayV2([-2, 0, 3, -5, 2, -1])
print(obj1.sumRange(2, 5))
print(obj2.sumRange(2, 5))