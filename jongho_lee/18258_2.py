from collections import deque
import sys 

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        if self.queue:
            print(self.queue.popleft())
        else:
            print(-1)
    
    def size(self):
        print(len(self.queue))

    def empty(self):
        print(int(len(self.queue) == 0))

    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)
    
    def back(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)

if __name__ == '__main__':
    input = sys.stdin.readline
    queue = Queue()
    op_dict = {
        'push' : queue.push, 
        'pop' : queue.pop, 
        'front' : queue.front, 
        'empty' : queue.empty, 
        'size' : queue.size,
        'back' : queue.back
    }
    n = int(input())
    for _ in range(n):
        usr_input = input().split()
        if len(usr_input) == 1:
            op_dict[usr_input[0]]()
        else:
            op_dict[usr_input[0]](usr_input[1])
