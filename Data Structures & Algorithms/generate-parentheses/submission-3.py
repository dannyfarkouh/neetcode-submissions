class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = [] 

        def backtrack(current, open_used, close_used):
            # Base Case 
            if open_used == n and close_used == n : 
                res.append(current)
            
            # recursive
            if open_used < n : 
                backtrack( current +'(', open_used+1, close_used )
            
            if close_used < open_used : 
                backtrack( current + ')', open_used, close_used+1 )
            
        backtrack('', 0, 0)

        return res
