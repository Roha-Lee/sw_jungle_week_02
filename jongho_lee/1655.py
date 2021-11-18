import sys 
from heapq import heappush, heappop

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    min_heap = []
    max_heap = []
    center = None
    for _ in range(n):
        user_input = int(input())
        if center == None:
            center = user_input
            print(center)
            continue

        if center >= user_input:
            heappush(max_heap, -user_input)
        else:
            heappush(min_heap, user_input)

        if len(max_heap) > len(min_heap):
            heappush(min_heap, center)
            center = -heappop(max_heap)
        elif len(max_heap) + 1 < len(min_heap):
            heappush(max_heap, -center)
            center = heappop(min_heap)
        
        print(center)
        