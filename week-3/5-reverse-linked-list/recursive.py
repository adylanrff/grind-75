# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        res = self.reverseList(head.next)  # get the last pointer
        next_node = head.next
        next_node.next = head
        head.next = None  # point to nothing to delete the cycle

        return res
