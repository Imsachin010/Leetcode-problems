# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index, L in enumerate(lists):
            if L is None:
                continue
            heapq.heappush(heap,(L.val,index,L))
        
        newhead= ListNode(-1)
        current = newhead

        while len(heap) > 0:
            _, index, node = heapq.heappop(heap)
        
            current.next = ListNode(node.val)
            current = current.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, index, node.next))
        return newhead.next