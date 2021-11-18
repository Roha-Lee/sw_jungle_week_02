import sys 
def count_area(n, board):
    global ones, zeros
    if n == 1:
        return board[0][0]
    curr_n = n // 2
    partitions = [[[0] * curr_n for _ in range(curr_n)] for _ in range(4)]

    for r in range(n):
        for c in range(n):
            position = (r // curr_n) * 2 + (c // curr_n)
            r_, c_ = r % curr_n, c % curr_n
            partitions[position][r_][c_] = board[r][c]
    
    left_top, right_top, left_bottom, right_bottom = partitions
    lt = count_area(curr_n, left_top)
    rt = count_area(curr_n, right_top)
    lb = count_area(curr_n, left_bottom)
    rb = count_area(curr_n, right_bottom)

    if lt == rt and rt == lb and lb == rb and rb == lt:
        return lt
    else:
        for val in [lt, rt, lb, rb]:
            if val == 1:
                ones += 1
            elif val == 0:
                zeros += 1
            
        

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]    
    ones, zeros = 0, 0 
    all_same = count_area(n, board)
    if all_same == 1:
        ones += 1
    elif all_same == 0:
        zeros += 1
    print(zeros)
    print(ones)