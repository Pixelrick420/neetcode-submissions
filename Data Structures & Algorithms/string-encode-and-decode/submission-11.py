class Solution:
    def encode(self, strs: List[str]) -> str:
        encoding = []
        for string in strs:
            length = len(string)
            encoding.append(f"{length:03d}")
            encoding.append(string)
        
        return ''.join(encoding)

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = len(s)
        index = 0

        while index < n:
            length = int(s[index : index + 3])
            decoded.append(s[index + 3 : index + 3 + length])
            index = index + 3 + length

        return decoded 