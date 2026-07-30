class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        longest = 0
        n = len(s)

        for right in range(n):
            while freq[s[right]]:
                freq[s[left]] -= 1
                left += 1
            
            freq[s[right]] += 1
            longest = max(longest, right - left + 1)
        
        return longest