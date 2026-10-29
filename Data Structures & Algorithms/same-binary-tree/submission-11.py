# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base Case: If both are None 
        if not p and not q : 
            return True 
        
        # If one of them is None 
        if not p or not q : 
            return False 
        
        # If both are there, but values differ
        if p.val != q.val : 
            return False 
        
        # If both are there and have the same values, then we recursively check the rest of the tree 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)