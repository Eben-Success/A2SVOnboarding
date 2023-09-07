# class MyStack:

#     def __init__(self):
#         self.stack = []
        

#     def push(self, x: int) -> None:
#         self.stack.append(x)
        

#     def pop(self) -> int:
#         if self.stack:
#             return self.stack.pop()
        

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]
        

#     def empty(self) -> bool:
#         return len(self.stack) == 0

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):

        self.head = None
        
    def push(self, x: int) -> None:
        newNode = ListNode(x)

        if not self.head:
            self.head = newNode
            newNode = self.head
            return

        cur = self.head
        while cur and cur.next:
            cur = cur.next
        cur.next = newNode


    def pop(self) -> int:
        if not self.head:
            return

        cur = self.head
        if cur.next is None:
            self.head = None
            return cur.val
        else:
            while cur.next and cur.next.next:
                cur = cur.next
            val = cur.next.val
            cur.next = None
            return val

        
    def top(self) -> int:
        if not self.head:
            return
        cur = self.head
        while cur and cur.next:
            cur = cur.next
        return cur.val


    def empty(self) -> bool:
        if not self.head:
            return True
        else:
            return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()