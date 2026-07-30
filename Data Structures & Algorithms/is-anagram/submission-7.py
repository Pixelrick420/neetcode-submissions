from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        if m != n:
            return False

        freq = defaultdict(int)
        for i in range(n):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        
        return all(freq[char] == 0 for char in freq.keys())
    