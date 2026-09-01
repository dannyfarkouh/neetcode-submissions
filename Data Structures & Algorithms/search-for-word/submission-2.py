class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs( r, c, word_len ) : 

            # base cases 
            if word_len == len(word) : 
                return True 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS : 
                return False
            if board[r][c] != word[word_len] or (r, c) in visited : 
                return False 
            
            # recursive step 
            visited.add((r, c))
            res = ((dfs(r+1, c, word_len+1)) or 
                    (dfs(r-1, c, word_len+1)) or 
                    (dfs(r, c+1, word_len+1)) or 
                    (dfs(r, c-1, word_len+1)))
            visited.remove((r,c))
                
            return res 
        
        for r in range(ROWS) :
            for c in range(COLS) : 
                if (r, c) not in visited : 
                    if dfs(r, c, 0) : 
                        return True 
        return False 