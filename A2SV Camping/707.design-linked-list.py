#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        count = 0

        cur = self.head

        while cur:
            cur = cur.next
            count += 1
            if count == index:
                return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        self.head = newNode
        newNode = self.head
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        cur = self.head

        while cur:
            cur = cur.next
        cur.next = newNode
        newNode.next = None
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        count = 0
        newNode = Node(val)

        while cur:
            cur = cur.next
            count += 1

            if count == index:
                nxt = cur.next
                cur.next = newNode
                newNode.next = nxt


    def deleteAtIndex(self, index: int) -> None:
        prev = None
        cur = self.head
        count = 0
        
        while cur:
            nxt = cur.next
            prev = cur
            cur = cur.next
            count += 1

            if count == index:
                cur.next = None
                prev.next = nxt

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# @lc code=end

