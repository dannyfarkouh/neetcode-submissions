class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # ROW 
        for i in range(9):
            seen = set() 
            for j in range(9): 
                if board[i][j] != ".": 
                    if board[i][j] in seen: 
                        return False 
                    else: 
                        seen.add(board[i][j])
                    
        # COLUMN 
        for i in range(9): 
            seen = set() 
            for j in range(9): 
                if board[j][i] != ".": 
                    if board[j][i] in seen: 
                        return False 
                    else: 
                        seen.add(board[j][i])

        # SQUARE 
        for x in range(9): # Because there are 9 squares in the grid 
            seen = set() 
            for i in range(3): 
                for j in range(3): 
                    row = (x // 3) * 3 + i 
                    col = (x % 3) * 3 + j 

                    if board[row][col] != ".": 
                        if board[row][col] in seen: 
                            return False 
                        else: 
                            seen.add(board[row][col])
        
        return True
