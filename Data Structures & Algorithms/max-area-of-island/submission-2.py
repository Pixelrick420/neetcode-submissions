class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def getArea(row, col):
            if (not (0 <= row < m and 0 <= col < n)) or (not grid[row][col]):
                return 0
            
            else:
                grid[row][col] = 0
                return 1 + (
                    getArea(row + 1, col) +
                    getArea(row - 1, col) + 
                    getArea(row, col + 1) + 
                    getArea(row, col - 1)
                )
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea = max(maxArea, getArea(i, j))
        
        return maxArea