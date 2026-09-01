class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {} 
        def dfs(remaining) : 

            if remaining == 0 : 
                return 0 
            
            if remaining < 0 : 
                return float("inf") 
            
            if remaining in cache : 
                return cache[remaining] 

            cache[remaining]  = float("inf")
            for coin in coins : 
                cache[remaining]  = min(cache[remaining] , 1 + dfs(remaining - coin))
            return cache[remaining]  
        
        ans = dfs(amount)
        return ans if ans != float("inf") else -1