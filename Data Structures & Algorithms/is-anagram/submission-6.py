class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if m != n:
            return False

        count = defaultdict(int)
        for i in range(n):
            count[s[i]] += 1
            count[t[i]] -= 1
        
        return all(count[char] == 0 for char in count.keys())