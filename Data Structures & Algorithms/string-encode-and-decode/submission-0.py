class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += (chr(len(s)) + s)
        return string

    def decode(self, s: str) -> List[str]:
        out = []
        stack = list(s[::-1])
        while stack:
            length = stack.pop()
            string = ''
            for i in range(ord(length)):
                string += stack.pop()
            out.append(string)
        return out