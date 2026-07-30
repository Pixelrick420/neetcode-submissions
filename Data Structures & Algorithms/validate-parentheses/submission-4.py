class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ')' : '(', ']' : '[', '}' : '{' }
        stack = []

        for char in s:
            if char not in pair:
                stack.append(char)
                continue
            
            if not stack or stack[-1] != pair[char]:
                return False
            
            else:
                stack.pop()
        
        return not stack