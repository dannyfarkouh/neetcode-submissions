class Solution:
    def rob(self, nums: List[int]) -> int:
        # either skip this house, or rob it and go to the next one 

        cache = {} 
        def dfs(i) : 

            # base case 
            if i >= len(nums) : 
                return 0 
            
            if i in cache : 
                return cache[i]
            
            cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return cache[i]

        return dfs(0)
