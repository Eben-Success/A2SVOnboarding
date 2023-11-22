from heapq import heappop, heappush, heapify

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = tail = ListNode(0)

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))

        heapify(heap)

        while heap:
            node_val, cur_idx, node = heap[0]

            if node == None:
                heappop(heap)

            next_node = node.next

            if node.next:
                heapreplace(heap, (next_node.val, cur_idx, next_node)) #replaces the smallest element with the cur val
            else:
                heappop(heap)

            tail.next = node
            tail = tail.next
        tail.next = None
        return dummy.next
