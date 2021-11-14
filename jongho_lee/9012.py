import sys 
def is_vps(usr_str):
    stack = []
    for letter in usr_str:
        if letter == '(':
            stack.append(0)
        else:
            if stack:
                stack.pop()
            else:
                return "NO"
    if stack: 
        return "NO"
    return "YES"


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        usr_input = input().rstrip()
        print(is_vps(usr_input))
