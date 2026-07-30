class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        n = len(chars)
        for i in range(n // 2):
            if chars[i] != chars[n - i - 1]:
                return False
        return True