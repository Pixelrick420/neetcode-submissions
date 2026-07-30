class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        water = 0

        while (left < right):
            if heights[right] < heights[left]:
                cur = (right - left) * heights[right]
                right -= 1
            else:
                cur = (right - left) * heights[left]
                left += 1

            water = max(water, cur)
        return water