class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = self.k
        self.dummy = ListNode(0)
        self.tail = self.dummy
        
        

    def enQueue(self, value: int) -> bool:
        newNode = ListNode(value)

        if self.size > 0:
            self.size -= 1
        else:
            return False

        self.tail.next = newNode
        self.tail = newNode

        return True
        

    def deQueue(self) -> bool:

        if self.size == self.k:
            return False

        else:

            if self.dummy.next:
                cur = self.dummy.next
                self.dummy.next = cur.next
                cur.next = None
                self.size += 1

                if self.dummy.next is None:
                    self.tail = self.dummy
                return True
        

    def Front(self) -> int:
        if self.dummy.next:
            return self.dummy.next.val
        return -1
        

    def Rear(self) -> int:
        if self.size == self.k: return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == self.k
        

    def isFull(self) -> bool:
        return self.size == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()