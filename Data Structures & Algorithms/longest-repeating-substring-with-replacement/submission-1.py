class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest = 0, 1
        n = len(s)
        freq = defaultdict(int)
        freq[s[0]] = 1
        mostfreq = 1

        for right in range(1, n):
            freq[s[right]] += 1
            mostfreq = max(mostfreq, freq[s[right]])

            while ((right - left + 1) - (mostfreq)) > k:
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest