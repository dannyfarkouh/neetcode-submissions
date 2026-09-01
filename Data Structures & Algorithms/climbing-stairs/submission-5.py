class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        res[0] = 0
        
        def dfs(total) : 

            # bc 
            if total > n : 
                return 

            if total == n : 
                res[0] += 1 
            
            return (dfs(total + 1) or dfs(total + 2))
        
        dfs(0)
        return res[0]