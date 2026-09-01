class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 
        visited = set() 

        def bfs(r, c) : 
            
            q = collections.deque() 
            q.append((r, c))
            visited.add((r, c))

            while q : 
                row, col = q.popleft()
                directions = [ [1,0], [0,1], [-1,0], [0,-1] ]

                for x, y in directions : 
                    r, c = row + x, col + y 

                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                        (r, c) in visited) or grid[r][c] != '1':
                        continue 
                    visited.add((r, c))
                    q.append((r, c))
               



        for r in range(ROWS) : 
            for c in range(COLS) : 
                if (r, c) not in visited and grid[r][c] == '1' : 
                    bfs(r, c)
                    islands += 1 
        return islands 