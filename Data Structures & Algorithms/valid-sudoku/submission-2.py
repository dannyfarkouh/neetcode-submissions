class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row 
        for row in range(9): 
            count = set() 
            for i in range(9):
                if board[row][i] == '.': 
                    continue
                if board[row][i] in count: 
                    return False 
                else: 
                    count.add(board[row][i])

        # column
        for col in range(9): 
            count = set() 
            for i in range(9): 
                if board[i][col] == '.': 
                    continue 
                if board[i][col] in count: 
                    return False 
                else: 
                    count.add(board[i][col])

        # square 
        for square in range(9): 
            count = set() 
            for i in range(3): 
                for j in range(3):
                    row = (square // 3) * 3 + i 
                    col = (square % 3) * 3 + j 

                    if board[row][col] == '.':
                        continue
                    if board[row][col] in count: 
                        return False 
                    else: 
                        count.add(board[row][col])
        return True 