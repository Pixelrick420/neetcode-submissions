class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        
        for _ in range(n):
            z =  x + y
            x = y
            y = z
                   
        return x