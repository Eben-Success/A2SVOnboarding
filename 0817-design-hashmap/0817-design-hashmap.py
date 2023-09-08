# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class MyHashMap:

#     def __init__(self):
#         self.head = None
        

#     def put(self, key: int, value: int) -> None:
#         flag = False
#         key = key % 10**6
#         newNode = ListNode([key, value])

#         if not self.head:
#             self.head = newNode
#             self.printer()
#             return

       
#         cur = self.head
#         while cur:
#             if cur.val[0] == key:
#                 cur.val[1] = value
#                 flag = True
#             cur = cur.next

#         if flag == False:
#             cur = self.head
#             while cur and cur.next:
#                 cur = cur.next
#             cur.next = newNode
#             return 
        

#     def get(self, key: int) -> int:
#         key = key % 10**6
#         cur = self.head

#         while cur:
#             if cur.val[0] == key:
#                 self.printer()
#                 return cur.val[1]
#             else:
#                 cur = cur.next
#         self.printer()
#         return -1
        

#     def remove(self, key: int) -> None:
#         cur = self.head
#         while cur and cur.next:
#             nxt = cur.next
#             if cur.val[0] == key:
#                 cur.next = nxt.next
#             cur = nxt




#     def printer(self):
#         cur = self.head
#         res = []
#         while cur:
#             res.append(cur.val)
#             cur = cur.next
#         print(res)     





class MyHashMap:

    def __init__(self):
        self.nums = [-1] * (pow(10, 6))
        

    def put(self, key: int, value: int) -> None:
        key = key % 10**6

        self.nums[key] = value 
        

    def get(self, key: int) -> int:
        key = key % 10**6
        return self.nums[key]

        
    def remove(self, key: int) -> None:
        key = key % 10**6
        self.nums[key] = -1
        



    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)