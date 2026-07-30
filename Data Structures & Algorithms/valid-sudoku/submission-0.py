class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)] 
        rows = [set() for _ in range(9)] 
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue

                if value in cols[j] or value in rows[i] or value in sub_boxes[i//3][j//3]:
                    return False
                
                cols[j].add(value)
                rows[i].add(value)
                sub_boxes[i//3][j//3].add(value)
        
        return True