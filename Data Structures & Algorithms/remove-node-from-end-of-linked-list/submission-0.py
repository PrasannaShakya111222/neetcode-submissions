# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        # Move right n + 1 steps ahead
        for _ in range(n + 1):
            right = right.next
        # Move both pointers until right reaches end
        while right:
            left = left.next
            right = right.next
        # Remove nth node from end
        left.next = left.next.next
        return dummy.next