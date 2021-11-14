import sys 
def find_min_distance(points, left, right):
    print(left, right)
    if left == right: 
        return float("inf")
    mid = (left + right) // 2
    min_dist = min(
                find_min_distance(points, left, mid-1), 
                find_min_distance(points, mid, right))
    print(min_dist)

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    points = sorted(points)
    find_min_distance(points, 0, len(points)-1)


