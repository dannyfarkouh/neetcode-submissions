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
        q.append([root, float("-inf"), float("inf")]) # each item of the queue will contain max value that that node can be 

        while q : 
            node, max_left, max_right = q.popleft() 

            if node : 

                if not max_left < node.val < max_right : 
                    return False 
                if node.left : 
                    q.append([node.left, max_left, node.val])
                if node.right : 
                    q.append([node.right, node.val, max_right])
        return True 