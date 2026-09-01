class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 

        for t in tokens : 
            if t == '+' : 
                e1, e2 = int(stack.pop()), int(stack.pop())
                stack.append(e1 + e2)
            elif t == '-' : 
                e1, e2 = int(stack.pop()), int(stack.pop())
                stack.append(e2 - e1)
            elif t == '*' : 
                e1, e2 = int(stack.pop()), int(stack.pop())
                stack.append(e1 * e2)
            elif t == '/' : 
                e1, e2 = int(stack.pop()), int(stack.pop())
                stack.append(int(float(e2) / e1))
            else: 
                stack.append(int(t))
        return stack[0]