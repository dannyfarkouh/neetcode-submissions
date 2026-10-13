# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        # Base case. If it does not pass, it means either p or q exists
        if not p and not q : 
            return True 

        # If it does not pass, it means both p and q exist        
        if not p or not q : 
            return False 
        
        # If it does not pass, it means p and q are equal, so we can keep recursing 
        if p.val != q.val : 
            return False 

        return ( self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) )