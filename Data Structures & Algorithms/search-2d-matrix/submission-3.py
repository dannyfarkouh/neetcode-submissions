class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix)-1

        row = [] 

        while top <= bottom : 

            middle_row = (top + bottom) // 2 

            if matrix[middle_row][-1] < target : 
                top = middle_row + 1 
            elif target < matrix[middle_row][0] : 
                bottom = middle_row - 1 
            
            elif target >= matrix[middle_row][0] and target <= matrix[middle_row][-1] : 
                row = matrix[middle_row] 
                break 

        # Now the row in which target should be = row 

        l, r = 0, len(row)-1 

        while l <= r : 
            mid = (l+r) // 2 

            if target < row[mid] : 
                r = mid - 1 
            elif target > row[mid] : 
                l = mid + 1 
            elif target == row[mid] : 
                return True 
        return False 