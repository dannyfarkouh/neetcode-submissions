class MinStack:

    def __init__(self):
        self.MinStack = [] 
        self.extraStack = [] 

    def push(self, val: int) -> None:
        self.MinStack.append(val) 
        if len(self.extraStack) == 0: 
            self.extraStack.append(val)
        else: 
            if self.extraStack[-1] > val: 
                self.extraStack.append(val)
            else: 
                self.extraStack.append(self.extraStack[-1])


    def pop(self) -> None:
        self.MinStack.pop()
        self.extraStack.pop() 

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.extraStack[-1]
