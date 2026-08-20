class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.out = set()

        def place(
            row: int, 
            cols: Set[int], 
            forward: Set[int], 
            backward: Set[int], 
            board: List[List[int]]
        ):
            if row >= n:
                solution = tuple()
                for i in range(n):
                    cur = ''
                    for j in range(n):
                        if board[i][j]:
                            cur += 'Q'
                        else:
                            cur += '.' 
                    solution += (cur,)
                
                self.out.add(solution)
                return

            for col in range(n):
                if (col in cols) or ((row - col) in forward) or ((col + row) in backward):
                    continue
                
                board[row][col] = 1
                cols.add(col)
                forward.add(row - col)
                backward.add(col + row)
                place(row + 1, cols, forward, backward, board)
                backward.remove(col + row)
                forward.remove(row - col)
                cols.remove(col)
                board[row][col] = 0
        
        place(0, set(), set(), set(), [[0] * n for _ in range(n)])

        return [list(val) for val in list(self.out)]

                            