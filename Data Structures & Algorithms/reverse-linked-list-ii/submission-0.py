# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        # Use dummy node to easily handle cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        # Move 'prev' to node right before 'left'
        for _ in range(left - 1):
            prev = prev.next
        # 'curr' starts at first node to be reversed
        curr = prev.next
        # Reverse sublist using standard pointer re-routing
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next