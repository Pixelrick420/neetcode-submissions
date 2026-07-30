class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = {}
        sublists = {}
        out = []

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            cur = tuple(count)
            if cur in signatures:
                out[sublists[signatures[cur]]].append(string)
            
            else:
                signatures[cur] = string
                sublists[string] = len(out)
                out.append([string])
        return out
