# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root : return None 

        res = self.inorder(root, [])
        return res[k-1]



    def inorder(self, root, arr) : 
        if not root : return arr
    
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    
        return arr
