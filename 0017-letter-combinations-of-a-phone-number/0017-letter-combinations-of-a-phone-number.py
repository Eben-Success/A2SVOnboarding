class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Time: O(4^n*n)

        hash = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9" :"wxyz"}

        res = []
        
        if not digits: return res

        def backtrack(i, cur):
            if len(cur) == len(digits):
                comb = "".join(cur)
                res.append(comb)
                return

            letters = hash[digits[i]]
            for letter in letters:
                backtrack(i+1, cur + [letter])

        backtrack(0, [])
        return res