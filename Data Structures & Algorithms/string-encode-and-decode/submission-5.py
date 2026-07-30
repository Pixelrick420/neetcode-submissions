class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            n = len(string)
            if n < 10:
                encoded.append("00" + str(n))
            elif n < 100:
                encoded.append("0" + str(n))
            else:
                encoded.append(str(n))
            encoded.append(string)
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        n = len(s)

        while index < n:
            length = ""
            string = ""
            for _ in range(3):
                length += s[index]
                index += 1
            
            length = int(length)
            for _ in range(length):
                string += s[index]
                index += 1
            decoded.append(string)
            
        return decoded