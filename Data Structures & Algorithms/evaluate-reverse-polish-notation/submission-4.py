class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {'+', '-', '/', '*'}
        stack = [] 

        for e in tokens: 
            if e not in oper: 
                stack.append(e)
            else: 
                if e == '+': 
                    e1 = int(stack.pop())
                    e2 = int(stack.pop())
                    stack.append(e2 + e1)
                elif e == '-': 
                    e1 = int(stack.pop())
                    e2 = int(stack.pop())
                    stack.append(e2 - e1)
                elif e == '/': 
                    e1 = int(stack.pop())
                    e2 = float(stack.pop())
                    stack.append(int(e2 / e1))
                elif e == '*': 
                    e1 = int(stack.pop())
                    e2 = int(stack.pop())
                    stack.append(e2 * e1)
        return int(stack[0])