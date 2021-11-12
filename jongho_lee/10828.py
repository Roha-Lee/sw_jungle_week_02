import sys 

class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0
    
    def push(self, x):
        self.stack.append(x)
        self.length += 1
    
    def pop(self):
        if self.length:
            self.length -= 1
            print(self.stack.pop())
        else:
            print(-1)
    
    def size(self):
        print(self.length) 

    def empty(self):
        print(int(self.length == 0))
        
    def top(self):
        if self.length:
            print(self.stack[-1])
        else:
            print(-1)

if __name__ == '__main__':
    input = sys.stdin.readline
    stack = Stack()
    op_dict = {
        'push': stack.push,
        'top': stack.top,
        'size': stack.size,
        'empty': stack.empty,
        'pop': stack.pop
    }
    
    n = int(input())
    for _ in range(n):
        usr_input = input().split()
        if len(usr_input) > 1:
            op_dict[usr_input[0]](usr_input[1])
        else:
            op_dict[usr_input[0]]()
    