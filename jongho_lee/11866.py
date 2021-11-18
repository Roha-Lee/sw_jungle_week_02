import sys
from collections import deque

def yoshepus_sequence(n, k):
    q = deque(range(1, n+1))
    result = []
    while len(q) > 1:
        for _ in range(k-1):
            q.append(q.popleft())
        result.append(q.popleft())
    result.append(q[0])
    return result


if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    result = yoshepus_sequence(n, k)
    print('<', end='')
    print(', '.join([str(num) for num in result]), end='')
    print('>')
