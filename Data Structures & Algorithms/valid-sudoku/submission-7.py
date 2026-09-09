class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows are all proper without duplicates 
        for row in range(9) : 
            seen = set()
            for i in range(9) : 
                if board[row][i] == '.' : 
                    continue 
                else : 
                    if board[row][i] in seen: 
                        return False 
                    else : 
                        seen.add(board[row][i])
        
        # Check cols are all proper without duplicates 
        for col in range(9) : 
            seen = set() 
            for i in range(9) : 
                if board[i][col] == '.' : 
                    continue 
                else : 
                    if board[i][col] in seen: 
                        return False 
                    else : 
                        seen.add(board[i][col])

        # Check 3x3 boxes are all proper without duplicates 
        for box in range(9) : # Number of boxes 
            seen = set() 
            for i in range(3) : # row 
                for j in range(3) : # col
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j 

                    if board[row][col] == '.' : 
                        continue 
                    else : 
                        if board[row][col] in seen : 
                            return False 
                        else : 
                            seen.add(board[row][col])
        
        return True 


                