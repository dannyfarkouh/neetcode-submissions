class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {} 
        def dfs(amount_used) : 
            
            if amount_used < 0 : 
                return float("inf")
            if amount_used == 0 : 
                return 0 
            
            if amount_used in cache : 
                return cache[amount_used]
            
            cache[amount_used] = float("inf")
            for coin in coins : 
                cache[amount_used] = min(cache[amount_used], 1 + dfs(amount_used-coin))
            return cache[amount_used]
            
        ans = dfs(amount)
        return ans if ans != float("inf") else -1
            