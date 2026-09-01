# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # base case 
        if not root : 
            return True 
        
        # BFS 
        q = collections.deque() 
        q.append([root, float("-inf"), float("inf")]) # represents node, and min and max value that it can take 
    
        while q : 
            node, max_l, max_r = q.popleft() 

            if node : 
                if not max_l < node.val < max_r : 
                    return False 
                if node.left : 
                    q.append([ node.left, max_l, node.val ])
                if node.right : 
                    q.append([ node.right, node.val, max_r ])
        return True 
