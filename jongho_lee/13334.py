import sys 
from heapq import heappush, heappop

def find_num_of_people_in_best_rail(rails, length):
    rails = sorted(rails, key = lambda x: x[1])
    prior_q = []
    best_num = 0
    for start, end in rails:
        threshold = end - length
        if start >= threshold:
            heappush(prior_q, start)
        while prior_q and prior_q[0] < threshold:
            heappop(prior_q)
        best_num = max(best_num, len(prior_q))
    return best_num

        
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    rails = []
    for _ in range(n):
        a, b = map(int, input().split())
        rails.append( (min(a, b), max(a, b)) )
    length = int(input())

    print(find_num_of_people_in_best_rail(rails, length))


## counter examples
## 50
## [[-34, 47], [-23, -15], [-38, -23]]
# def find_num_of_people_in_best_rail(rails, n, length):
#     q = sorted(rails)
#     prior_q = []
#     best_num = 0
#     for idx, (start, end) in enumerate(q):
#         if end - start > length:
#             continue
    
#         while prior_q:
#             prev_start, prev_end = heappop(prior_q)
#             if prev_start >= start:
#                 heappush(prior_q, (prev_start, prev_end))
#                 break
        
#         if not prior_q:
#             heappush(prior_q, (start, end))
        
#         end_point = start + length
#         for i in range(idx + len(prior_q), n):
#             next_start, next_end = q[i]
#             if next_end <= end_point:
#                 heappush(prior_q, (next_start, next_end))
#             else:
#                 break
        
#         if best_num < len(prior_q):
#             best_num = len(prior_q)
        
#     return best_num
