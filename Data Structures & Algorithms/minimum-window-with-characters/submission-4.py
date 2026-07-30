class Solution:
    def minWindow(self, s: str, t: str) -> str:
        out, minLength = [-1, -1], float('inf')
        freq = defaultdict(int)

        for char in t:
            freq[char] += 1
        
        chars = set(t)
        have, need = 0, len(chars)
        left, n = 0, len(s)
        
        for right in range(n):
            freq[s[right]] -= 1

            if s[right] in chars and freq[s[right]] == 0:
                have += 1
            
            while have == need:
                if (right - left + 1) < minLength:
                    minLength = (right - left + 1)
                    out = [left, right]
                
                freq[s[left]] += 1
                if s[left] in chars and freq[s[left]] > 0:
                    have -= 1
                left += 1
        
        left, right = out
        return s[left : right + 1] if minLength != float('inf') else ""
