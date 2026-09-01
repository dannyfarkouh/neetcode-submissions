class MinStack:

    def __init__(self):
        self.MinStack = [] 
        self.currMinStack = [] 

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        
        if len(self.currMinStack) == 0: 
            self.currMinStack.append(val)
        else: 
            if val < self.currMinStack[-1]: 
                self.currMinStack.append(val)
            else: 
                self.currMinStack.append(self.currMinStack[-1])


    def pop(self) -> None:
        self.MinStack.pop()
        self.currMinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.currMinStack[-1]
        