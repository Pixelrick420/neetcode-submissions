class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        for char in s1:
            freq[char] += 1
        
        left = 0
        m, n = len(s1), len(s2)

        subfreq = defaultdict(int)
        for right in range(n):
            char = s2[right]
            subfreq[char] += 1

            while subfreq[char] > freq[char]:
                subfreq[s2[left]] -= 1
                left += 1
            
            if (right - left + 1 >= m):
                return True
        
        return False