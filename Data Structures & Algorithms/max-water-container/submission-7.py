class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right = n - 1

        out = 0
        while left < right:
            height = min(heights[left], heights[right])
            out = max(out, (right - left) * height)

            if height == heights[left]:
                left += 1
            
            else:
                right -= 1
        
        return out
