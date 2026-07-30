class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        out = 0

        while left < right:
            if heights[left] < heights[right]:
                area = (right - left) * heights[left]
                out = max(out, area)
                left += 1
            
            else:
                area = (right - left) * heights[right]
                out = max(out, area)
                right -= 1
        
        return out