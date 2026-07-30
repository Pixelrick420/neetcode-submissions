class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for index, height in enumerate(heights):
            start = index
            while(stack and stack[-1][1] >= height):
                start = stack[-1][0]
                area = max(((index - start) * stack[-1][1]), area)
                stack.pop()
                
            stack.append((start, height))
        
        n = len(heights)
        while stack:
            start = stack[-1][0]
            area = max(((n - start) * stack[-1][1]), area)
            stack.pop()

        return area