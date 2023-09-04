class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        n = len(tokens)
        tokens.sort()
        left, right = 0, n - 1
        cur_score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                cur_score += 1
                left += 1

                max_score = max(max_score, cur_score)

            elif cur_score > 0:
                if power < tokens[right]:
                    power += tokens[right]
                    cur_score -= 1
                    right -= 1

            else:
                break

        return max_score


        