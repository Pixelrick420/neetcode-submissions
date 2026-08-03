class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        
        while n:
            if n & 1:
                out += 1
            
            n >>= 1
        
        return out

    def countBits(self, n: int) -> List[int]:
        counts = [0]
        for num in range(1, n + 1):
            counts.append(self.hammingWeight(num))
        
        return counts
