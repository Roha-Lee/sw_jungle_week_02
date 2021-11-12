import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find = list(map(int,sys.stdin.readline().split()))

def binary_search(arr,find,start,end):
    
    if start > end :
        return 0
    
    if find < arr[start] or find > arr[end]:
        return 0
   
    mid = (start + end)//2
    
    if arr[mid] == find:
        return 1
    elif arr[mid] > find :
        return binary_search(arr,find,start,mid-1)
    
    else :
        return binary_search(arr,find,mid+1,end)     
A = sorted(A)
for i in range(len(find)) :
    result = binary_search(A,find[i],0,N-1)
    print(result)
        
