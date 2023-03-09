# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        newhead = ListNode(-1, head)
        fast = newhead
        slow = newhead

        while fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
            slow = slow.next

            if fast.next == slow.next:
                break
        
        if fast.next is None:
            return None
        
        slow = newhead
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        
        return slow.next
