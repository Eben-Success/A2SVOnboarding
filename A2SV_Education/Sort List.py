# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # the head is None
        if not head:
            return head

        # If len(head) <= 1: return head else: contine
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if count > 1:
                break
        
        if count == 1:
            return head

        slow, fast = head, head
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        

        while fast and fast.next:
            tail = tail.next
            slow = slow.next
            fast = fast.next.next

        tail.next = None
        second = slow
        first = dummy.next

        L = self.sortList(first)
        R = self.sortList(second)
        return self.mergeSortedList(L, R)

        
    def mergeSortedList(self, list1, list2) -> Optional[ListNode]:

        res = ListNode(0)
        cur = res

        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next

            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2

        return res.next

        
        
