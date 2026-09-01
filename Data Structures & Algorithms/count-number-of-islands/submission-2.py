class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid : return 0 
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        res = 0 

        def bfs(r, c) :
            q = collections.deque() 
            q.append((r, c))

            while q : 
                row, col = q.popleft() 
                directions = [ [0,1], [1,0], [-1,0], [0,-1] ]

                for x, y in directions : 
                    r, c = row+x, col+y

                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                        grid[r][c] != '1' or (r, c) in visited) :
                        continue 
                    q.append((r, c))
                    visited.add((r, c)) 


        for r in range(ROWS) : 
            for c in range(COLS) : 
                if grid[r][c] == '1' and (r, c) not in visited : 
                    bfs(r, c)
                    res += 1 
        return res 