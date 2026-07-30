class Solution:
    def trap(self, heights: List[int]) -> int:
        left, blocks, water = 0, 0, 0
        n = len(heights)

        for right in range(1, n):
            if heights[right] >= heights[left]:
                water += (heights[left] * (right - left - 1) - blocks)
                blocks = 0
                left = right
            
            else:
                blocks += heights[right]

        right, blocks = n - 1, 0
        for left in range(n - 2, -1, -1):
            if heights[left] > heights[right]:
                water += (heights[right] * (right - left - 1) - blocks)
                blocks = 0
                right = left
            
            else:
                blocks += heights[left]
        
        return water
