from collections import deque

class MyQueue:

    def __init__(self):
        self.stack_1 = deque() # 
        self.stack_2 = deque() # flipped one 

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        self.__fill()
        return self.stack_2.pop()
        
    def peek(self) -> int:
        self.__fill()
        return self.stack_2[-1]
        
    def empty(self) -> bool:
        return len(self.stack_1) == 0 and len(self.stack_2) == 0
    
    def __fill(self):
        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()