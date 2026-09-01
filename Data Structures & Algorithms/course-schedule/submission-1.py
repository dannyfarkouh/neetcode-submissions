class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Check if there is a cycle in the graph 

        # Initialize the preMap that maps every node to its neighbors 
        preMap = { i:[] for i in range(numCourses) } 

        # fill up the preMap 
        for crs, pre in prerequisites :
            preMap[crs].append(pre)
        # preMap contains key = course, value = list of prerequisites

        visited = set()
        
        def dfs( crs ) : 

            # base case 
            if crs in visited : 
                return False 

            if preMap[crs] == [] :
                return True 
            
            visited.add(crs)
            for pre in preMap[crs] : 
                if not dfs(pre) : 
                    return False 
            visited.remove(crs)
            preMap[crs] = [] 
            return True 
        
        for crs in range(numCourses) : 
            if not dfs(crs) : return False 
        return True 