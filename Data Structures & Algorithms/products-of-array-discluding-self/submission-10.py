class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        
        left = [1 for i in range(l)]
        right = [1 for i in range(l)]
        res = [1 for i in range(l)]

        # Left to right 
        for i in range(1, l) : 
            left[i] = nums[i-1] * left[i-1]
        
        # right to left 
        for i in range(l-2, -1, -1) : 
            right[i] = nums[i+1] * right[i+1]
        
        # res 
        for i in range(l) : 
            res[i] = left[i] * right[i] 
        
        return res 