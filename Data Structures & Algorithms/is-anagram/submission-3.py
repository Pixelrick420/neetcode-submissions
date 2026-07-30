class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1
            
        return all(count[char] == 0 for char in t)