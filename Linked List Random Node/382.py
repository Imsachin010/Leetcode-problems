# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head 

    def getRandom(self) -> int:
        k = 1
        current = self.head
        while current is not None:
            if random.randint(1, k) <= 1:
                keep = current.val

            current = current.next
            k +=1
        return keep


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()      