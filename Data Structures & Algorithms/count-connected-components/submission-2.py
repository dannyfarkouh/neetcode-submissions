class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # init adj 
        adj = [ [] for _ in range(n) ]

        res = 0 

        # fill adj 
        for u, v in edges : 
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set() 
        
        def dfs(node) : 

            # bc 
            for nei in adj[node] : 
                if nei not in visited : 
                    visited.add(nei) 
                    dfs(nei)
        
        for node in range(n) : 
            if node not in visited : 
                dfs(node)
                res += 1 

        return res 