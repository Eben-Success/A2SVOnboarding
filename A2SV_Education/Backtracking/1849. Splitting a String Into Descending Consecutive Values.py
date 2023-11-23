class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtrack(cur_idx, prev_idx):
            if cur_idx == n:
                return True
            
            for j in range(cur_idx, n):
                val = int(s[cur_idx:j+1])
                if val + 1 == prev_idx and backtrack(j+1, val):
                    return True
            return False

        for i in range(n - 1):
            val = int(s[:i+1])
            if backtrack(i+1, val):
                return True
        return False
