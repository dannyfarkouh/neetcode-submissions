class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length 
        stack = [] # [temp, i]

        for i, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][0]: 
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temp, i])
        return res 