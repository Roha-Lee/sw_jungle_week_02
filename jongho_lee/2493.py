import sys 
def received_tower_index(towers, n):
    results = [0] * n
    stack = []
    for i in range(len(towers)-1, -1, -1):
        stack.append((i, towers.pop()))
        while towers and stack and towers[-1] >= stack[-1][1]:
            idx, _ = stack.pop()
            results[idx] = i    
    return results

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    towers = list(map(int, input().split()))
    print(*received_tower_index(towers, n))
    