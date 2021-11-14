import heapq
import sys 
from heapq import heappush, heappop

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    q = []
    for _ in range(n):
        user_input = int(input())
        if user_input == 0:
            if q:
                print(-heappop(q))
            else:
                print(0)
        else:
            heappush(q, -user_input)