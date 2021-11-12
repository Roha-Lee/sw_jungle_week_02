from statistics import median_low, median_high
import sys
import heapq
from collections import deque
num_house , num_wifi = list(map(int,sys.stdin.readline().split()))
house_list = [int(sys.stdin.readline()) for _ in range(num_house)]
house_list.sort()
wifi_index_list = []
global cnt
cnt = 0



def wifi_search(arr,start,end,n):
    global cnt

    if n-2 == cnt:
        return
    mid  = median_low(arr)
    mid_index = arr.index(mid)
    wifi_index_list.append(mid)
    cnt += 1
    wifi_search(arr,start,mid_index,n)
    wifi_search(arr,mid_index,end,n)

wifi_index_list.append(house_list[0])
wifi_search(house_list,0,num_house,num_wifi)
wifi_index_list.append(house_list[-1])

wifi_index_list.sort()
# print(wifi_index_list)
min_distance = 10000000000
for i in range(len(wifi_index_list)-1):
    if min(wifi_index_list[i+1]-wifi_index_list[i],min_distance) < min_distance:
        min_distance = min(wifi_index_list[i+1]-wifi_index_list[i],min_distance)

print(min_distance)
    
        
        