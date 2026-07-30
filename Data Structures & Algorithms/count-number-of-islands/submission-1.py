class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def explore(row, col):
            grid[row][col] = '0'

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '0':
                    print(nr, nc)
                    explore(nr, nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    explore(i, j)

        return count