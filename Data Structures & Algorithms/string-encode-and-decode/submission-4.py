class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            strlen = len(string)
            if strlen < 10:
                encoded += "00"
            elif strlen < 100:
                encoded += "0"
            
            encoded += str(strlen)
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        index = 0
        strings = []

        while index < len(s):
            num = int(s[index:(index + 3)])
            index += 3
            strings.append(s[index:(index + num)])
            index += num
            
        return strings
            
            