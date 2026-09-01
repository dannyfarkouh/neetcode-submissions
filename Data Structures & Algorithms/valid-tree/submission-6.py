class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree = no cycles and cannot be two separate trees 

        # ajdacency hashmap key = node, value = neighbors
        adj = [ [] for i in range(n) ]

        # fill up adjacency hashmap 
        for u, v in edges :
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set() 

        # We keep count of the parent because the parent does not count as a cycle when checking. 
        def dfs(node, parent) : 

            # BC 
            if node in visited : 
                return False 
             
            visited.add(node)
            for n in adj[node] : 
                if n == parent : 
                    continue 
                if not dfs(n, node) : 
                    return False 
            return True 
        
        # we check if len(visited) == n to see if there is one tree or two separate ones. 
        return dfs(0,-1) and len(visited) == n 