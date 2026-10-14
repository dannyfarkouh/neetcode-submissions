# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy 

        # 1 - Get the right pointer to move n times 
        right = head 
        while n > 0 and right : 
            right = right.next 
            n-=1 
        
        # Now right moved n times to the right. We can have a left pointer, move both right and left towards the end. 
        # This way, once right touches the end, left will be at the node that we want to remove from the linked list
        # This is because the distance between left and right is exactly n, and right is at the end of the linked list, so left is n from the end, 
        # This is exactly what the problem is looking for 

        while right : 
            left = left.next 
            right = right.next 
        
        # Now left is the node right before the one that needs to be removed (this is because left starts at dummy, which is a node before head.)
        # If left was starting at head exactly, then left would be the node we have to remove. 
        left.next = left.next.next 

        return dummy.next 