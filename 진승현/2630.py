import sys

N = int(sys.stdin.readline()) # 종이 한변의 길이
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  #종이 전체의 0,1 값 

result = [] #결과 합산 배열

def solution(x, y, N) :
  color = paper[x][y] #color는 paper 0,0부터 돈다.
  for i in range(x, x+N) : # 행이 x 부터 n까지
    for j in range(y, y+N) : # 열이 y부터 n까지
      if color != paper[i][j] : #하나라도 첫 시작 color과 다른게 나오면
        solution(x, y, N//2) #4등분으로 쪼갠다
        solution(x, y+N//2, N//2) #2번째 분면
        solution(x+N//2, y, N//2) #3번째 분면
        solution(x+N//2, y+N//2, N//2) #4번째 분면
        return # return 재귀 탈출 조건
  if color == 0 :
    result.append(0)
  else : #color 이 1이면
    result.append(1)


solution(0,0,N) #첫 호출
print(result.count(0))
print(result.count(1))
