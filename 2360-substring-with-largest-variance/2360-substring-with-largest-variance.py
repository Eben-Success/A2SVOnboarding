class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        global_max = 0
        
        for i in range(26):
            for j in range(26):
                # major and minor cannot be the same, and both must appear in s.
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue
                
                # Find the maximum variance of major - minor.
                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                major_count = 0
                minor_count = 0
                
                # The remaining minor in the rest of s.
                rest_minor = counter[j]
                
                for ch in s:
                    if ch == major:
                        major_count += 1
                    if ch == minor:
                        minor_count += 1
                        rest_minor -= 1
                    
                    # Only update the variance if there is at least one minor.
                    if minor_count > 0:
                        global_max = max(global_max, major_count - minor_count)
                    
                    # We can discard the previous string if there is at least one remaining minor.
                    if major_count < minor_count and rest_minor > 0:
                        major_count = 0
                        minor_count = 0
        
        return global_max
