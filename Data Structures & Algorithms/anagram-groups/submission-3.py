class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            signature = tuple(count)
            signatures[signature].append(string)
        
        return [signatures[sign] for sign in signatures.keys()]