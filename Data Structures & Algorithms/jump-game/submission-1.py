class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cache = {} 
        def dfs(i) : 

            if i == len(nums)-1 : 
                return True 
            
            if nums[i] == 0 : 
                return False
            
            if i in cache : 
                return cache[i]

            for j in range(1, nums[i]+1) : 
                cache[i] = dfs(i + j) 
                if cache[i] :  
                    return True 
            return False 

        return dfs(0) if nums else None 