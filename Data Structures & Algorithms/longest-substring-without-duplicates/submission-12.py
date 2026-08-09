from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        n = len(s)

        left = 0
        out = 0

        for right in range(n):
            while (freq[s[right]] > 0):
                freq[s[left]] -= 1
                left += 1
            
            freq[s[right]] += 1
            out = max(out, right - left + 1)
        
        return out