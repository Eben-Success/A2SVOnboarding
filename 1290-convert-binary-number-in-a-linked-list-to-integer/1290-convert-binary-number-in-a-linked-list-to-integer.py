# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if not head:
            return 0
        
        nums = []
        
        cur = head
        
        while cur:
            nums.append(cur.val)
            cur = cur.next
            
        return self.convertBinToDecimal(nums)
            
    
    def convertBinToDecimal(self, binary):
        
        res = i = 0
      
        binary = int("".join(str(num) for num in binary))
        
        print(binary)
        
        while binary != 0:
            last = binary % 10
            last = last * pow(2, i)
            res += last
            binary //= 10
            i += 1
        return res
        