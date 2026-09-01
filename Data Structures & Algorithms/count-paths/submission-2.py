class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}
        def dfs(x, y) : 
            
            if (x < 0 or y < 0 or x >= m or y >= n ) : 
                return 0 
            
            if ( x == m-1 and y == n-1 ) : 
                return 1 
            
            if (x, y) in cache : 
                return cache[(x, y)]
            
            cache[(x, y)] = (dfs(x+1, y) + dfs(x, y+1))
            return cache[(x, y)] 
        
        return dfs(0,0)