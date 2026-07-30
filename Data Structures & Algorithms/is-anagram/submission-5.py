class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        for char in t:
            freq[char] -= 1
        
        for char in freq.keys():
            if freq[char]:
                return False
        return True
        
