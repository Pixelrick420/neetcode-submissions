from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord("a")] += 1

            sign = tuple(freq)
            groups[sign].append(string)
            
        out = []
        for sign in groups.keys():
            out.append(groups[sign])
        
        return out