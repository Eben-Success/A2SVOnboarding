# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        list1 = self.reverseList(l1)
        list2 = self.reverseList(l2)
        carry = 0

        while list1 or list2 or carry:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0

            val = (val1 + val2 + carry)

            num = val % 10
            carry = val // 10

            newNode = ListNode(num)
            tail.next = newNode
            tail = tail.next

            if list1:list1 = list1.next
            if list2: list2 = list2.next

        tail.next = None

        return self.reverseList(dummy.next)


        


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        