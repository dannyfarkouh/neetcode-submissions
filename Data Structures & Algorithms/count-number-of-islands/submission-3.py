class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # vars 
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        islands = 0 

        def bfs(r, c) : 

            q = collections.deque() 
            q.append((r, c))
            visited.add((r, c))

            while q : 
                row, col = q.popleft()

                dirs = [ [1,0], [0,1], [-1,0], [0,-1] ]

                for x, y in dirs : 
                    r, c = row + x, col + y 

                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                        (r, c) in visited or grid[r][c] != '1') : 
                        continue 
                    else : 
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(ROWS) :
            for c in range(COLS) : 
                if grid[r][c] == '1' and (r, c) not in visited : 
                    bfs(r, c)
                    islands +=1 

        return islands 