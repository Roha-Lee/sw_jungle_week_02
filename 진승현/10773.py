import sys
stack = []
result = 0
K = int(sys.stdin.readline())

while K > 0 :
    num = int(sys.stdin.readline())
    
    if num != 0:
        stack.append(num)
        result += num
    else :
        if len(stack) > 0:
            x = stack.pop()    
            result -= x 
        
            
    K -= 1
    
print(result)    
