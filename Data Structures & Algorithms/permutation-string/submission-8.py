class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        for char in s1:
            freq[char] += 1
        
        left = 0
        n, m = len(s2), len(s1)

        for right in range(n):
            while freq[s2[right]] <= 0:
                freq[s2[left]] += 1
                left += 1
            
            freq[s2[right]] -= 1
            if (right - left + 1) == m:
                return True
        return False
