"""
Minimum Time to Visit Points

Calculate minimum time to visit all points in order on a 2D plane.
Movement: 8 directions (including diagonal), 1 unit time per step.
Algorithm: Chebyshev distance (max of coordinate differences).
"""

def main(points: list[list[int]]) -> int:
    """
    Calculate minimum time to visit all points in order.
    
    Args:
        points (list[list[int]]): List of [x, y] coordinates to visit in order
                                 
    Returns:
        int: Minimum time required to visit all points
        
    Algorithm:
        Uses Chebyshev distance: for each consecutive pair of points,
        time = max(|x2-x1|, |y2-y1|) because diagonal movement is allowed.
        Sum all pairwise times.
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> main([[1, 1], [3, 4], [-1, 0]])
        7  # (1,1)->(3,4): max(2,3)=3, (3,4)->(-1,0): max(4,4)=4, Total: 7
    
    Note: Modifies input list using pop().
    """
    total_time  = 0

    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        total_time += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    
    return total_time

print(main([[1, 1], [3, 4], [-1, 0]]))
