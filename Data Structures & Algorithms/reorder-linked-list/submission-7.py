# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1 - find the middle point of the linked list 
        slow, fast = head, head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
        
        # Slow is now the mid point 
        mid = slow.next 
        slow.next = None 
    
        # 2 - reverse the second half 
        prev, curr = None, mid 
        while curr : 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        
        # the two heads of both halves of the linked list
        first, second = head, prev 

        while first and second : 
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 

            first = tmp1 
            second = tmp2 
