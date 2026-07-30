class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        left, longest = 0, 1
        n = len(s)
        freq = defaultdict(int)
        maxfreq = 1
        freq[s[0]] = 1

        for right in range(1, n):
            char = s[right]
            freq[char] += 1

            maxfreq = max(maxfreq, freq[char])

            while ((right - left + 1) - (maxfreq)) > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left, + 1)

        return longest + 1

