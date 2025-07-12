from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.queue = deque()
        self.running_sum = 0
        
    def count(self):
        return len(self.queue)
    
    def isFull(self):
        return self.count() == self.window
    
    def add(self, val: int):
        if self.isFull():
            self.running_sum -= self.queue.popleft()
        self.queue.append(val)
        self.running_sum += val
    
    def movingSum(self):
        return self.running_sum / self.count() if self.queue else 0
        
    def next(self, val: int) -> float:
        self.add(val)
        return self.movingSum()
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)