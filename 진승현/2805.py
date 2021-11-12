import sys
def binary_search(arr,find,start,end):
    
    while start <= end :
       
        mid = (start + end)//2 # 절단 높이
        log = 0
        
        for i in arr:
            if i > mid :
                log += (i - mid)
    
              
        if log >= find : #자르고 가져갈 나무의 합이 필요한 나무길이보다 길다. 너무 밑으로 잘랐다. 올려서 자르자
            global answer
            start = mid+1 # 절단높이를 올리자
            answer = mid  
            
        else :
            end = mid-1 # 잘랐더니 너무 많이 잘랐다. 절단 높이를 낮추자

    
N,M = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))
tree = sorted(tree)
answer = 0

binary_search(tree,M,0,tree[-1]) 
print(answer)
