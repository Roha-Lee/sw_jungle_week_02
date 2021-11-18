import sys 
def calculate_num_area(intervals):
    coordinates = []
    stacks = []
    for left, right in intervals:
        coordinates.append((0, left))
        coordinates.append((1, right))
    coordinates = sorted(coordinates, reverse=True)
    coordinates = sorted(coordinates, key=lambda x: x[1])
    count = 1
    
    for lr, x in coordinates:
        if lr == 0:
            stacks.append((0, x))
        else:
            inner_circle = 0
            while stacks and stacks[-1][0] == 2:
                _, complete_circle = stacks.pop()
                inner_circle += complete_circle
            
            new_circle = x - stacks.pop()[1]
            if new_circle == inner_circle:
                count += 2    
            else:
                count += 1
            stacks.append((2, new_circle))
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    intervals = []
    for _ in range(n):
        x, r = map(int, input().split())
        intervals.append((x-r, x+r))
    print(calculate_num_area(intervals))
