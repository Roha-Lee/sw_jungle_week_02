import sys 
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
class Queue:
    def __init__(self, max_length=2000000):
        self.queue = [0] * max_length
        self.head = 0
        self.tail = 0
    
    def push(self, x):
        self.queue[self.tail] = x
        self.tail += 1

    def pop(self):
        if self.head == self.tail:
            print(-1)
        else:
            print(self.queue[self.head])
            self.head += 1
        
    def size(self):
        print(self.tail - self.head)
    
    def empty(self):
        print(int(self.head == self.tail))

    def front(self):
        if self.head == self.tail:
            print(-1)
        else:
            print(self.queue[self.head])
    
    def back(self):
        if self.head == self.tail:
            print(-1)
        else:
            print(self.queue[self.tail-1])


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
