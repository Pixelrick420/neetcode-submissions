class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        out = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                if pile % mid:
                    hours += (pile // mid) + 1
                else:
                    hours += (pile // mid)

            if hours <= h:
                right = mid - 1
                out = mid
            
            else:
                left = mid + 1
            
            
        
        return out