class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest, left = 0, 0
        n = len(s)
        maxFreq = 0

        for right in range(n):
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])

            while ((right - left + 1) - maxFreq) > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest
