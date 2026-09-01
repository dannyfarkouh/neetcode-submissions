class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for e in tokens: 
            if e == '+': 
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif e == '-': 
                e1, e2 = int(stack.pop()), int(stack.pop())
                stack.append(e2 - e1)
            elif e == '*': 
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif e == '/': 
                e1, e2 = int(stack.pop()), int(stack.pop())
                stack.append(int(float(e2)/e1))
            else: 
                stack.append(int(e))
        return stack[0]