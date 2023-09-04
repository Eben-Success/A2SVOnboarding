
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
            if count == index:
                return cur.val
            count += 1
            cur = cur.next
        # self.printList()
        return -1
    
        
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
        # self.printList()
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.addAtHead(val)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        
        # self.printList()
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        
        if index == 0:
            self.addAtHead(val)
            return 
        
        cur = self.head
        count = 0
        
        while cur:
            if count == index - 1:
                newNode.next = cur.next
                cur.next = newNode
            cur = cur.next
            count += 1
        # self.printList()
            
            


    def deleteAtIndex(self, index: int) -> None:
        if not self.head: return 
        
        if index == 0:
            self.head = self.head.next
            return 
            
        count = 0
        cur = self.head
        
        while cur:
            if count == index - 1 and cur.next:
                cur.next = cur.next.next
            cur = cur.next
            count += 1
            
        # self.printList()
            
    # def printList(self):
    #     cur = self.head
    #     res = []
    #     while cur:
    #         res.append(cur.val)
    #         cur = cur.next
    #     print(res)
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


