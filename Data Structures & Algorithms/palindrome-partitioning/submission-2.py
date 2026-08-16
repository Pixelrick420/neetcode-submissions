from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def isPalindrome(string: str) -> bool:
            n = len(string)
            for i in range(n // 2):
                if string[i] != string[n - i - 1]:
                   return False

            return True 

        @cache
        def divide(index: int) -> List[List[str]]:
            if index >= n:
                return []

            substrings = []
            for clip in range(index + 1, n + 1):
                if isPalindrome(s[index: clip]):
                    parts = divide(clip)
                    new = [s[index : clip],]
                    if not parts:
                        substrings.append(new)

                    else:
                        for part in parts:
                            substrings.append(new  + part)

            return substrings
        
        return divide(0)

