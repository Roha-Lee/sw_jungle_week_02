import sys

T = int(sys.stdin.readline())
while T > 0 :
    stack = []
    ps = str(sys.stdin.readline().strip()) # strip없으면 배열이 비어보여도 공백이 하나의 문자로 들어가 len 1이 찍힌다.
    for i in ps :
        if i == '(':
            stack.append(i)
            
        else :
            if len(stack) != 0  :
                stack.pop()
                
            else :
                stack.append(i)
                break
    
    
    
    if   not stack :
        print("YES")
    else :
        print("NO")      
                
    
    T -= 1
