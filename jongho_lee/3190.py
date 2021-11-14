import sys 
from collections import deque
def move_one_step(snake, board, dr, dc):
    rows = len(board)
    cols = len(board[0])
    cr, cc = snake[-1]
    nr, nc = cr + dr, cc + dc
    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != 0:
        snake.append((nr, nc))
        if board[nr][nc] != 2:
            pr, pc = snake.popleft()
            board[pr][pc] = 1
        board[nr][nc] = 0
        return True
    return False
    
def get_survive_time(board, moves):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    snake = deque(((0, 0),))
    dr, dc, d_idx = 0, 1, 0 
    count = 0
    move_time, move_dir = moves.popleft()
    while move_one_step(snake, board, dr, dc):
        count += 1
        if count == move_time:
            if move_dir == 'D':
                d_idx += 1    
            else:
                d_idx -= 1
            d_idx %= 4
            dr, dc = directions[d_idx]
            if moves:
                move_time, move_dir = moves.popleft()
            else:
                move_time, move_dir = -1, None
                
    return count + 1

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    board = [[1] * n for _ in range(n)]
    board[0][0] = 0
    k = int(input())
    for _ in range(k):
        r, c = map(int, input().split())
        board[r-1][c-1] = 2
    l = int(input())
    moves = [input().split() for _ in range(l)]
    moves = deque(map(lambda x:(int(x[0]), x[1]), moves))
    print(get_survive_time(board, moves))