class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1

            sign = tuple(freq)
            signatures[sign].append(string)
        
        out = []
        for sign in signatures.keys():
            out.append(signatures[sign])
        
        return out