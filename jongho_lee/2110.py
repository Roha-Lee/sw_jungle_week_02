import sys 
def is_possible_arrange(home_locations, distance, num):
    start = home_locations[0]
    for home_location in home_locations:
        if home_location - start >= distance:
            start = home_location
            num -= 1
    return num <= 1

if __name__ == '__main__':
    input = sys.stdin.readline
    n, c = map(int, input().split())
    home_locations = sorted([int(input())for _ in range(n)])
    left = 1
    right = home_locations[-1] - home_locations[0]
    best = 0
    while left <= right: 
        mid = (left + right) // 2
        if is_possible_arrange(home_locations, mid, c):
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    print(best)