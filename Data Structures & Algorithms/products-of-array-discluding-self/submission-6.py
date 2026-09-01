class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        in_order = [] 
        out_order = [] 

        for i in range(len(nums)): 
            if i == 0: 
                in_order.append(nums[i])
            else: 
                in_order.append(in_order[i-1]*nums[i])
        
        for i in range(len(nums)-1, -1, -1): 
            if i == len(nums)-1: 
                out_order.append(nums[i])
            else: 
                out_order = [nums[i] * out_order[0]] + out_order 

        res = [] 

        for i in range(len(nums)): 
            if i == 0: 
                res.append(out_order[1])
            elif i == len(nums)-1: 
                res.append(in_order[i-1])
            else: 
                res.append(in_order[i-1] * out_order[i+1])
        return res 