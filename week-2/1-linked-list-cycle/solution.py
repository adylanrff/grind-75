# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow_pointer = head 
        if head.next:
            fast_pointer = head.next.next
        else:
            return False
        
        while slow_pointer != fast_pointer and slow_pointer and fast_pointer:
            slow_pointer = slow_pointer.next
            
            if fast_pointer.next != None:
                fast_pointer = fast_pointer.next.next
            else:
                fast_pointer = None

        return slow_pointer == fast_pointer