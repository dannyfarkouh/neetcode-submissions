class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # To track which positions in the board are currently on our path, since we cannot take the same path twice 
        path = set() 

        def dfs( r, c, i ) : 

            # If we have finished finding our word 
            if i == len(word) : 
                return True 
            
            # Here are all the reasons to backtrack 
            # if the row or column are out of bounds 
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS) : 
                return False 
            # if the letter that we are on in the board is the wrong letter 
            if word[i] != board[r][c] :
                return False 
            # if we go over the same positions that we already went on in our path 
            if (r, c) in path : 
                return False 

            path.add((r, c))
            res = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or 
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1))
            path.remove((r, c))
            return res 
        
        for r in range(ROWS) : 
            for c in range(COLS) : 
                if dfs(r, c, 0) : return True 
        return False 