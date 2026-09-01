from functools import cache 

class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}  
        def dfs(total) : 

            # base case 
            if total > n : 
                return 0

            if total == n : 
                return 1  
            
            if total in cache : 
                return cache[total]
            
            cache[total] = (dfs(total + 1) + dfs(total + 2))
            return cache[total]

        return dfs(0)
        