class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def find(row, col, index, visited):
            if board[row][col] != word[index]:
                return False

            elif index >= len(word) - 1:
                return True

            else:              
                visited.add((row, col))

                for dr, dc in directions:
                    nr, nc = (row + dr), (col + dc)
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and find(nr, nc, index + 1, visited):
                        return True
                
                visited.remove((row, col))
            
            return False
        
        for i in range(m):
            for j in range(n):
                if find(i, j, 0, set()):
                    return True
        
        return False
