class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        n = len(digits)

        def compute(index: int) -> List[str]:
            if index >= n:
                return []
            
            digit = digits[index]
            nxt = compute(index + 1)
            possible = []

            if not nxt:
                    return letters[digit].copy()

            for letter in letters[digit]:
                for suffix in nxt:
                    possible.append(letter + suffix)
            
            return possible
        
        return compute(0)

            
