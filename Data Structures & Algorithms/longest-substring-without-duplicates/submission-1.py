class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        charset = set()
        left = 0
        out = 1
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            
            charset.add(s[right])
            out = max(out, len(charset))
        return out