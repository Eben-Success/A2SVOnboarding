# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        1. Create dummy node and point to head.
        2. Set tail to dummy and cur to head.
        3. Condition while cur and cur.next:
        4. Check if cur.val == cur.next.val.
        5. Use another while loop to get the duplicates.
        6. set the tail.next to the next of the cur.
        Done!!!!
        """

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                tail.next = cur
            else:
                cur = cur.next
                tail = tail.next

        return dummy.next

        

        




        
        