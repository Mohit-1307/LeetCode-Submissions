# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push first node of each list
        for i, node in enumerate(lists):
            if node:
                # (value, index, node)
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:

            val, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            # Push next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next