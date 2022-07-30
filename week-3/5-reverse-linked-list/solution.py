# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        prev = None
        cur_node = head
        next_node = cur_node.next

        while cur_node.next != None:
            next_node = cur_node.next  # 2
            cur_node.next = prev  # None
            prev = cur_node  # 1
            cur_node = next_node  # 2

        cur_node.next = prev

        return cur_node
