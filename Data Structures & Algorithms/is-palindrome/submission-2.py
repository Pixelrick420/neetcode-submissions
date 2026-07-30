class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = str()
        for char in s:
            if char.isalpha():
                string += char.lower()
            elif char.isdigit():
                string += char
        
        n = len(string)
        for i in range(n):
            if string[i] != string[n - i - 1]:
                return False
        return True