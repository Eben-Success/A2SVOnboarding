class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        """
        Use two pointers.
        if char at s < char at t: increment s pointer.
        elif char at s > char at t: increment s pointer.
        elif chat at s == char at t: increment s and t pointer.
        return len(t) - r
        """

        # Time: O(n) | Space: O(1)

        l, r = 0, 0

        while l < len(s) and r < len(t):

            if s[l] < t[r]:
                l += 1

            elif s[l] == t[r]:
                l += 1
                r += 1

            elif s[l] > t[r]:
                l += 1

        return len(t) - r
