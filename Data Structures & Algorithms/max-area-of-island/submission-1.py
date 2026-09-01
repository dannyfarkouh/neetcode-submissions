class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 

        def bfs(r, c) : 
            max_islands = 1 
            q = collections.deque() 
            q.append((r, c))
            visited.add((r, c))

            while q : 
                row, col = q.popleft() 
                directions = [ [1, 0], [0,1], [-1,0], [0,-1] ]

                for x, y in directions : 
                    r, c = row + x, col + y 

                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                        grid[r][c] != 1 or (r, c) in visited) : 
                        continue 
                    else : 
                        visited.add((r, c))
                        q.append((r, c))
                        max_islands+=1 
            return max_islands
    
        res = 0 
        for r in range(ROWS) : 
            for c in range(COLS) : 
                if grid[r][c] == 1 and (r, c) not in visited : 
                    res = max(res, bfs(r, c))
        return res 