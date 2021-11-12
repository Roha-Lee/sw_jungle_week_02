import sys
N,C = map(int,sys.stdin.readline().split())
house = []
for i in range(N):
    house.append(int(sys.stdin.readline()))

house = sorted(house)    #집 좌표 정렬

def BinarySearch(arr, val, start, end):
    
    while start <= end: #start랑 end 같게 되면
        mid = (start + end) // 2 #위치 기반으로 찾는 것이지만 여기서는 최대인접거리를 표현.
        last_iptime = arr[0]
        count =1
    
        for i in range(1,len(arr)):
            if arr[i] - last_iptime >=  mid : #0번집과 1번집이 가장 인접하지 않기에 통과
                count +=1 #공유기 놓았다.
                last_iptime = arr[i] # 공유기 설치된 위치 저장
    
        if count >= val: #공유기 너무 많다 최대인접거리를 늘리자.
            global answer 
            start = mid +1
            answer = mid #count 랑 val이랑 같을 수도 있으니 answer에 mid 저장
          
        else:
            end = mid -1 # 공유기 너무 적다 최대인접거리를 좁히자.
            

end = house[-1] - house[0] # 현재 최대 인접 거리
answer = 0
start =1


BinarySearch(house,C,start,end)
print(answer)            
            
