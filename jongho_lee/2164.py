import sys 
from collections import deque

def remain_num(q):
    while len(q) > 1:
        q.popleft()
        if not q:
            break
        q.append(q.popleft())
    return q[0]


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    q = deque(range(1, n+1))
    print(remain_num(q))
    