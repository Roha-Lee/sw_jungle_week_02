import sys
from collections import deque

t = int(input())

for _ in range(t):
    
    vps = list(map(str,sys.stdin.readline().strip().split()))
    if vps[-1] == "(" or vps[0]==")":
        print("NO")
    else:
        
        while len(vps) > 1:
            stack1 = deque([])
            stack2 = deque([])
            if vps[-1] == vps[-2] and stack1[-1] == vps[-1]:
                stack1.append(vps.pop())
            elif vps[-1] == vps[-2] and stack1[-1] != vps[-1]:
                print("NO")
                break
            elif len(stack1) == 0 or stack1[-1] == vps[-1]:
                stack1.append(vps.pop())
            else:
                comparelist = list(map(lambda x : ")" if x == "(" else"(", stack1))
                if vps[-1:-len(stack1)-1:-1] == comparelist:
                    del vps[-1:-len(stack1)-1:-1]
                else:
                    print("NO")
                    break
