# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head

        while fast and n > 0:
            fast = fast.next
            n -= 1

        slow = head

        dummy = ListNode(0)
        dummy.next = head
        slow = head
        tail = dummy

        while fast:
            slow = slow.next
            fast = fast.next
            tail = tail.next

        tail.next = slow.next
        slow.next = None

        return dummy.next
        


        
