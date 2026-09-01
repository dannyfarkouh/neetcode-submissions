# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1 - Find the middle point 

        slow, fast = head, head.next 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
        # Second is the middle point 
        second = slow.next 
        slow.next = None 

        # 2 - Reverse the second half 

        prev, curr = None, second 
        while curr : 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        # Now prev = head of the second reversed half 

        first, second = head, prev 
        while second : 
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1 

            first = temp1 
            second = temp2 
            
