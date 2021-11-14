import sys 

def ceil_1000(R):
    rows = len(R)
    cols = len(R[0])
    for r in range(rows):
        for c in range(cols):
            R[r][c] %= 1000
    return R


def matrix_mult(A, B):
    A_rows = len(A)
    A_cols = len(A[0])
    B_cols = len(B[0])
    R = [[0] * B_cols for _ in range(A_rows)]
    for i in range(A_rows):
        for j in range(B_cols):
            val = 0
            for k in range(A_cols):
                val += A[i][k] * B[k][j]
            R[i][j] = val
    R = ceil_1000(R)
    return R


def matrix_exp(A, n):
    if n == 1:
        return ceil_1000(A)
    
    if n % 2 == 1:
        return matrix_mult(A, matrix_exp(A, n-1))
    
    temp_result = matrix_exp(A, n//2)
    
    return matrix_mult(temp_result, temp_result)


if __name__ == '__main__':
    input = sys.stdin.readline
    n, b = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result_matrix = matrix_exp(matrix, b)
    for r in range(n):
        print(' '.join(list(map(str, result_matrix[r]))))
        
    