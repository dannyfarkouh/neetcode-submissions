class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjMap = { i : [] for i in range(n) }

        for u, v in edges : 
            adjMap[u].append(v)
            adjMap[v].append(u)


        visited = set() 
        res = 0 
        def dfs(i) : 

            for nei in adjMap[i] : 
                if nei not in visited : 
                    visited.add(nei)
                    dfs(nei)
        
        for i in range(n) : 
            if i not in visited : 
                dfs(i)
                res += 1
        return res 
                    