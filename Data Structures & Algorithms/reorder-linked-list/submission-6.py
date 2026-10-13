# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # First, find the middle point 
        slow, fast = head, head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 

        # Get the middle point
        middle = slow.next 
        # Remove connection to the first half
        slow.next = None 

        # Second, reverse the second half 
        prev, curr = None, middle 

        while curr : 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        
        # The head of the first half is head, the head of the second (reversed) half is prev
        first, second = head, prev 

        while second : 
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1

            first = temp1 
            second = temp2 
            