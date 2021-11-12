import sys 
def longest_common_subsequence(seqs, n):
    DP = [0] * n
    DP[0] = 1
    for i in range(1, n):
        DP[i] = 1
        for j in range(i):
            if seqs[i] > seqs[j]:
                DP[i] = max(DP[j] + 1, DP[i])
    return max(DP)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    seqs = list(map(int, input().split()))
    print(longest_common_subsequence(seqs, n))