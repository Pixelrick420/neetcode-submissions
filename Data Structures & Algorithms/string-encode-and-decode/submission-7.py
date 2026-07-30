class Solution:
    def encode(self, strs: List[str]) -> str:
        # encoded = []

        # for string in strs:
        #     length = len(string)
        #     if length < 10:
        #         lenStr = '00' + str(length)
        #     elif length < 100:
        #         lenStr = '0' + str(length)
        #     else:
        #         lenStr = str(length)
            
        #     encoded.append(lenStr)
        #     encoded.append(string)
        
        # return ''.join(encoded)
        self.strings = strs
        return ''

    def decode(self, s: str) -> List[str]:
        return self.strings
        # decoded = []
        # length = len(s)
        # index = 0

        # while index < length:
        #     lenStr = s[index : index + 3]
        #     curLen = int(lenStr)
        #     index += 3

        #     string = s[index : index + curLen]
        #     decoded.append(string)
        #     index += curLen
        
        # return decoded