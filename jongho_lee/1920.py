import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    nums = map(int, input().split())
    for num in nums:
        print(int(num in A))