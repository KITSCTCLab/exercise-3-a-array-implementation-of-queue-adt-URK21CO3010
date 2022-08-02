class Solution():
    
    def __init__(self, sizeArg):
        self.size = sizeArg
        self.front = -1
        self.rear = -1
        self.queue = []
        self.stack = []
    
    def pop(self):
            x = self.stack.pop()
            return x
    
    def push(self, item):
            self.stack.append(item)
    
    def dequeue(self):
            self.front += 1
            x = self.queue.pop()
            return x
    
    def enqueue(self, item):
            self.rear += 1
            self.queue.append(item)

string = "rotator"

solution = Solution(len(string))

for char in string:
    solution.enqueue(char)
    solution.push(char)

size = 6

retval = True

for i in range(size):
    queueItem = solution.dequeue()
    stackItem = solution.pop()
    if queueItem == stackItem:
        continue
    else:
        retval = False

print(retval)
