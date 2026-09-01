# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1- find the middle point 

        slow, fast = head, head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None 

        # reverse the second half 
        curr, prev = second, None 

        while curr : 
            
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        # head2 is the head of the second half 
        first, second = head, prev 

        while second : 

            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1

            first = temp1 
            second = temp2 



