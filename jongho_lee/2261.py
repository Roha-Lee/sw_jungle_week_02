import sys 

def distance_square(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def find_min_distance(points):
    if len(points) == 1: 
        return float('inf')
    
    mid = len(points) // 2
    mid_distance = min(
        find_min_distance(points[:mid]), 
        find_min_distance(points[mid:])
    )
    mid_candidates = []
    for x, y in points:
        if (points[mid][0] - x) ** 2 < mid_distance:
            mid_candidates.append((x, y))
    
    mid_candidates = sorted(mid_candidates, key=lambda x: x[1])
    for i in range(len(mid_candidates)):
        _, i_y = mid_candidates[i]
        for j in range(i+1, len(mid_candidates)):
            _, j_y = mid_candidates[j]
            if (j_y - i_y) ** 2 < mid_distance:
                curr_dis = distance_square(mid_candidates[i], mid_candidates[j])
                if curr_dis < mid_distance:
                    mid_distance = curr_dis
            else:
                break

    return mid_distance


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    points = sorted(points)
    print(find_min_distance(points))