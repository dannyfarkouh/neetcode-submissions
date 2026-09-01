class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs( r, c, visited, prevHeight ) :

            #Base Case 
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or heights[r][c] < prevHeight ) :
                return 

            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # top row, bottom row 
        for c in range(COLS) : 
            dfs( 0, c, pac, -1 )
            dfs(ROWS-1, c, atl, -1)
        
        # left col, right col
        for r in range(ROWS) : 
            dfs( r, 0, pac, -1 )
            dfs( r, COLS-1, atl, -1 )
        
        res = [] 
        for r in range(ROWS) : 
            for c in range(COLS) : 
                if (r, c) in atl and (r, c) in pac : 
                    res.append([r, c])
        return res 