class Solution:
    def findComplement(self, num: int) -> int:
        res = num ^  (2 ** num.bit_length()) - 1
        return res
        
