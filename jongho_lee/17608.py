import sys 
def count_from_left(stack):
    count = 0 
    curr_num = -float("inf")
    
    while stack:
        if stack[-1] <= curr_num:
            stack.pop()
        else:
            count += 1
            curr_num = stack.pop()

    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    
    stack = []
    for _ in range(n):
        stack.append(int(input()))
    
    print(count_from_left(stack))
    
