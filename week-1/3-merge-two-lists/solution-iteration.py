# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        prev = dummy_head
        
        cur_node_1 = list1
        cur_node_2 = list2
        
        while cur_node_1 != None and cur_node_2 != None:
            if cur_node_1.val < cur_node_2.val:
                prev.next = cur_node_1
                cur_node_1 = cur_node_1.next
            else:
                prev.next = cur_node_2
                cur_node_2 = cur_node_2.next
            prev = prev.next
        
        if cur_node_2 is None:
            prev.next = cur_node_1
        
        if cur_node_1 is None:
            prev.next = cur_node_2
        
        return dummy_head.next
