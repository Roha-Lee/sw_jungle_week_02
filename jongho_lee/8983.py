import sys
from bisect import bisect_left

def count_animal(animals, shots, shot_range):
    count = 0
    for x, y in animals:
        idx1 = bisect_left(shots, x)
        idx2 = idx1 - 1 if idx1 - 1 >= 0 else 0
        idx1 = idx1 if idx1 < len(shots) else idx1 - 1
        if shot_range - y >= abs(x - shots[idx1]) or shot_range - y >= abs(x - shots[idx2]):
            count += 1 
    return count 


if __name__ == '__main__':
    input = sys.stdin.readline
    m, n, l = map(int, input().split())
    shots = sorted(list(map(int, input().split())))
    animals = [tuple(map(int, input().split())) for _ in range(n)]
    print(count_animal(animals, shots, l))
    