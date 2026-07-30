class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char not in brackets:
                stack.append(char)
            
            elif not stack or stack[-1] != brackets[char]:
                return False
            
            else:
                stack.pop()
        
        return not stack