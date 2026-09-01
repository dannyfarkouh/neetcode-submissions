class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1 : 
            return nums[0]
        
        cache = {} 
        def dfs(i, flag) : 

            if i >= len(nums) : 
                return 0 
            
            if i == len(nums)-1 and flag : 
                return 0

            if (i, flag) in cache : 
                return cache[(i, flag)] 
            
            cache[(i, flag)] = max(nums[i] + dfs(i+2, flag), dfs(i+1, flag))
            return cache[(i, flag)]
        
        return max( dfs(0, True), dfs(1, False) )
            