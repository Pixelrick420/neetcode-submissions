class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.out = []
        def generate(string, open_count, closed_count):
            if open_count == n and closed_count == n:
                self.out.append(string)
                return
            
            if open_count < n:
                generate(string + '(', open_count + 1, closed_count)
            
            if closed_count < open_count:
                generate(string + ')', open_count, closed_count + 1)
        
        generate('', 0, 0)
        return self.out