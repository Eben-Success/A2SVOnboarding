# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = self.reverseList(slow)

        cur1 = head
        cur2 = half
        max_val = 0

        while cur1 and cur2:
            max_val = max(max_val, (cur1.val + cur2.val))
            cur1 = cur1.next
            cur2 = cur2.next

        return max_val


    def reverseList(self, node):
        prev = None
        cur = node

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
        