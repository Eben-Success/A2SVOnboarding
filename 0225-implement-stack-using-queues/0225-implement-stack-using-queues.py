class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.dummy = ListNode(0)
        

    def push(self, x: int) -> None:
        newNode = ListNode(x)

        newNode.next = self.dummy.next
        self.dummy.next = newNode

    def pop(self) -> int:
        nxt = self.dummy.next
        self.dummy.next = nxt.next
        nxt.next = None
        return nxt.val

        
    def top(self) -> int:
        return self.dummy.next.val
        

    def empty(self) -> bool:
        return not self.dummy.next
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()