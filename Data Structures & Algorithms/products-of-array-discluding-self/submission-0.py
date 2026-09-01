class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        order = []
        reverse = [] 

        for i in range(len(nums)): 
            if i == 0: 
                order.append(nums[i])
            else: 
                order.append(nums[i] * order[i-1])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1: 
                reverse.append(nums[i])
            else: 
                reverse = [nums[i] * reverse[0]] + reverse
        
        res = []
        for i in range(len(nums)): 
            if i == 0: 
                res.append(reverse[1])
            elif i == len(nums)-1: 
                res.append(order[i-1])
            else: 
                res.append(order[i-1] * reverse[i+1])
        return res
