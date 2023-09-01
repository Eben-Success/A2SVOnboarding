# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = self.reverseList(slow)
        
        cur1 = head
        cur2 = second

        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True



    def reverseList(self, head: Optional[ListNode]):

        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    def printList(self, head):
        res = []
        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)
        
