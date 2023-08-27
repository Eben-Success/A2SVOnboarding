# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        cur = head
        cur = head.next

        count = 0

        while cur:
            count += cur.val
            if cur.val == 0:
                newNode = ListNode(count)
                count = 0
                tail.next = newNode
                tail = tail.next
            cur = cur.next

        return dummy.next





        

            