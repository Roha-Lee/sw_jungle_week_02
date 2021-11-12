from statistics import median_low, median_high
import sys
import heapq
from collections import deque
num_house , num_wifi = list(map(int,sys.stdin.readline().split()))
house_list = [int(sys.stdin.readline()) for _ in range(num_house)]
house_list.sort()
wifi_index_list = set()

def wifi_search(arr,start,end,n):
    
    if (start + end) % 2 == 0:
        mid  = (start + end) // 2
    else:
        mid = (start + end) // 2
        if min(arr[end]-arr[mid],arr[mid]-arr[start]) < min(arr[end]-arr[mid+1],arr[mid+1]-arr[start]):
            mid += 1
    if n == 3:
        wifi_index_list.add(start)
        wifi_index_list.add(end)
        wifi_index_list.add(mid)
        return
    
    wifi_index_list.add(mid)
    n -= 1
    wifi_search(arr,start,mid,n)
    wifi_search(arr,mid,end,n)

wifi_search(house_list,0,4,4)
print(wifi_index_list)
    
        
        