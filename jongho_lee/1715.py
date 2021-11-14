import sys 
from heapq import heappush, heappop, heapify

def get_card_compare_num(cards):
    q = cards[:]
    heapify(q)
    
    count = 0 
    while len(q) > 1:
        num1 = heappop(q) 
        count += num1 
        if q: 
            num2 = heappop(q)
            count += num2
            heappush(q, num1 + num2)
        
    return count

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    cards = [int(input()) for _ in range(n)]
    print(get_card_compare_num(cards))