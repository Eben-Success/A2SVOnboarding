class Solution:
    def romanToInt(self, s: str) -> int:

        num = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        count = 0
        for i in range(1, len(s)):
            if num[s[i-1]] > num[s[i]]:
                count += num[s[i-1]]
            elif num[s[i-1]] < num[s[i]]:
                count -= num[s[i-1]]
            
            elif num[s[i-1]] == num[s[i]]:
                count += num[s[i-1]]

        count += num[s[-1]]
        return count

