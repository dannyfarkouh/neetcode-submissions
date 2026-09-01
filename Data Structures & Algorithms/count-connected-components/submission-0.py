class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [ [] for _ in range(n) ]
        visited = set() 

        for u, v in edges : 
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(node) : 
            for n in adj[node] : 
                if n not in visited : 
                    visited.add(n) 
                    dfs(n)
        

        res = 0 
        for node in range(n) : 
            if node not in visited : 
                visited.add(node) 
                dfs(node)
                res += 1 
            
        return res 