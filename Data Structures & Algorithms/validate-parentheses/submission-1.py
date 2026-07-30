class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'{':'}', '(':')','[':']'}
        for char in s:
            if char in pairs:
                stack.append(char)
            
            elif (not stack) or char != pairs[stack[-1]]:
                return False
            
            else:
                stack.pop()

        return (not stack)