import sys

def find_closest_two_value(liquids):
    left, right = 0, len(liquids) - 1
    best = float('inf')
    num1, num2 = 0, 0
    while left < right: 
        val = liquids[left] + liquids[right]
        if best > abs(val):
            best = abs(val)
            num1, num2 = liquids[left], liquids[right]
        if val > 0:
            right -= 1
        else:
            left += 1
    return num1, num2

 
if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input())
    liquids = sorted(list(map(int, input().split())))
    
    print(*find_closest_two_value(liquids))
