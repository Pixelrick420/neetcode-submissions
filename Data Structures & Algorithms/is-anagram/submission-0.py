class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        n = len(s)
        if n != len(t):
            return False

        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1
        
        for char in counts.keys():
            if counts[char] != 0 :
                return False
        
        return True
