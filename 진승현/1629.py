#모듈로 거듭제곱법 이런게 있었다니..
import sys
def solution(X,Y):
    if Y == 1:
        return X % C
    else :
        temp = solution(X,Y//2) #X^(Y//2)를 미리 구한다.
        if Y % 2 ==0:
            return temp * temp % C
        else:
            return temp * temp * X % C    

A,B,C = map(int,sys.stdin.readline().split())

answer = solution(A,B)
print(answer)
