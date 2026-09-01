class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res_max = nums[0]
    
        for i in range(len(nums)) : 
            cur_max = 0 
            for j in range(i, len(nums)) : 
                cur_max += nums[j]
                res_max = max(res_max, cur_max)
        return res_max 