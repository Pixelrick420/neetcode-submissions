class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = {}
        out = []

        for string in strs:
            sign = [0] * 26
            for char in string:
                sign[ord(char) - ord('a')] += 1
            
            sign = tuple(sign)
            if sign in signatures:
                out[signatures[sign]].append(string)

            else:
                signatures[sign] = len(out)
                out.append([string])

        return out 