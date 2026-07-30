class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        left = 0
        longest = 0
        out = 1

        for right in range(n):
            freq[s[right]] += 1
            longest = max(longest, freq[s[right]])

            while (right - left + 1) - longest > k:
                freq[s[left]] -= 1
                left += 1
            
            out = max(out, right - left + 1)
            
        return out
                