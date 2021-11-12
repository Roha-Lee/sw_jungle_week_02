import  sys
N = int(sys.stdin.readline())
list1 = []
stack = []
for i in range(N):
    list1.append(int(sys.stdin.readline().strip()))


stack.append(list1[-1])
  

for i in range(N-1,-1,-1):
    if stack[-1] < list1[i]:
        stack.append(list1[i])
        
print(len(stack))    
    
