class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        out = 0


        while (left < right):
            length = min(heights[left], heights[right])
            width = (right - left)
            out = max(out, length * width)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return out