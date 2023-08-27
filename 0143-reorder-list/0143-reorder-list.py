# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head.next: return head

        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        second_half = self.reverseList(slow)

        dummy = tail = ListNode(0)
        cur1 = head
        cur2 = second_half

      

        while cur1 or cur2:
            if cur1:
                tail.next = cur1
                cur1 = cur1.next
                tail = tail.next

            if cur2:
                tail.next = cur2
                cur2 = cur2.next
                tail = tail.next


    def reverseList(self, node):

        prev = None
        cur = node

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt


        return prev