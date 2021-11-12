import sys
N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))
X= sorted(X)
def search_zero():
    left,right = 0, N-1 # 입력된 N개의 X인덱스 0부터 끝까지
    zero_point = sys.maxsize #시스템상 최고값
    result = [0,0] # 빈 배열 선언
    
    while left < right : # 둘이 서로 만날때까지
        twosum = X[left] + X[right]
        abs_sum = abs(twosum) #절대값을 구한다.
        
        if zero_point > abs_sum: # 두 값의 절대값을 비교한다.
            zero_point = abs_sum
            result = [left,right] #최저 절대값의 인덱스 기억해 놓기
            
        if twosum > 0 : #두 합이 양수이면 0에 가까워져야함으로 right가 음수쪽으로 온다.
            right -= 1
        else : #두 합이 음수이면 0에 가까워져야함으로 left가 양수쪽으로 온다.
            left += 1
    return result            # left right가 만날때가 오고 그때 while 끝난다. 시간복잡도(n)

zero1,zero2 = search_zero()
print(X[zero1],X[zero2])
