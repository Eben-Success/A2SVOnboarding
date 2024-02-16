class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
      
    #     a = self.DecToBin(x)
    #     b = self.DecToBin(y)

    #     a = "0" * (max(len(a), len(b)) - len(a)) + a
    #     b = "0" * (max(len(a), len(b)) - len(b)) + b

    #     count = 0

    #     for i in range(len(a)):
    #         if a[i] != b[i]:
    #             count += 1

    #     return count
        
    # def DecToBin(self, n: int) -> int:
    #     res = ""

    #     while n:
    #         res += str(n & 1)
    #         n >>= 1
    #     return res[::-1]

        return (x ^ y).bit_count()
        
