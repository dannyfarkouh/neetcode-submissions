class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n 
        def dfs(total) : 

            if total == n : 
                return 1
            
            if total > n : 
                return 0 

            if cache[total] != -1 : 
                return cache[total]
    
            cache[total] = dfs(total+1) + dfs(total+2)
            return cache[total]

        return dfs(0)