class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)

        for char in t:
            need[char] += 1

        n = len(s)
        left = 0
        shortest = n + 1
        out = s
        

        for right in range(n):
            need[s[right]] -= 1
            
            while (left < right and need[s[left]] < 0):
                need[s[left]] += 1
                left += 1

            if all(need[char] <= 0 for char in need.keys()) and (right - left + 1) < shortest:
                shortest = right - left + 1
                out = s[left : right + 1]    
        
        return "" if shortest > n else out