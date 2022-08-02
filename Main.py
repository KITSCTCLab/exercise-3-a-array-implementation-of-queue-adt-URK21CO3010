class Solution():
    
    def __init__(self, sizeArg):
        self.size = sizeArg
        self.front = -1
        self.rear = -1
        self.queue = []
        self.stack = []
    
    def pop(self):
        if not self.is_stack_empty():
            x = self.stack.pop()
            return x
    
    def push(self, item):
        if not self.is_stack_full():
            self.stack.append(item)
    
    def dequeue(self):
        if not self.is_queue_empty():
            self.front += 1
            x = self.queue[self.front]
            return x
    
    def enqueue(self, item):
        if not self.is_queue_full():
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
