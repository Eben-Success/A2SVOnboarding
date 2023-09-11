
class Solve:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        n = len(s)
        for i in range(n):
            even_len = self.get_palindrome(s, i, i + 1)
            odd_len = self.get_palindrome(s, i, i)
            res = max([even_len, odd_len, res], key=len)
        return res
    
    def get_palindrome(s: str, l: int, r: int) -> str:

        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l:r+1]
    


soln = Solve()
s = "babad"
print(soln.longestPalindrome(s))

