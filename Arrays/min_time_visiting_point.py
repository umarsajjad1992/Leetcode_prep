def main(points: list[list[int]]) -> int:
    total_time  = 0

    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        total_time += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    
    return total_time

print(main([[1, 1], [3, 4], [-1, 0]]))
