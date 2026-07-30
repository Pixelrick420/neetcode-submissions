class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        n = len(s)
        length = n + 1
        substring = ""
        freq = defaultdict(int)
        curfreq = defaultdict(int)
        chars = len(set(t))
        cur = 0

        for char in t:
            freq[char] += 1
        
        for right in range(n):
            curfreq[s[right]] += 1
            if curfreq[s[right]] == freq[s[right]]:
                cur += 1
            
            while (cur >= chars and curfreq[s[left]] > freq[s[left]]):
                curfreq[s[left]] -= 1
                left += 1

            if cur >= chars and (right - left + 1) < length:
                length = (right - left + 1)
                substring = s[left : (right + 1)]
        
        
        return substring
                


        
