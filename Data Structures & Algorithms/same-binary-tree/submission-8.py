# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # If this does not pass, p or q is not None 
        if not p and not q : 
            return True 
        
        # If this does not pass, both p and q are not None 
        if not p or not q : 
            return False 
        
        # If this does not pass, p and q are the same 
        if p.val != q.val : 
            return False 

        # If all the previous checks pass, it means that p and q are the same, so we dig deeper in recursion 
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))