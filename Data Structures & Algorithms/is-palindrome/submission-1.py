class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        string = []

        for char in s:
            if char in chars:
                string.append(char.lower()) 

        n = len(string)
        for i in range(n // 2):
            if string[i] != string[n - i - 1]:
                return False
        
        return True