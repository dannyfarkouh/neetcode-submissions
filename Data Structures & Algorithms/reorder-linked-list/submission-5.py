# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1- find the middle 

        slow, fast = head, head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None 

        # 2- Reverse the second half
        curr, prev = second, None  

        while curr : 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        # prev is the head of the second reversed linked list 

        first, second = head, prev 

        while second : 
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1 

            first = temp1 
            second = temp2 