class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsets = [set() for _ in range(9)]
        colsets = [set() for _ in range(9)]
        subsets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if(
                    (cur != '.') and 
                    (
                        (cur in rowsets[i]) or
                        (cur in colsets[j]) or
                        (cur in subsets[3 * (i // 3) + (j // 3)])
                    )
                ):
                    return False
                rowsets[i].add(cur)
                colsets[j].add(cur)
                subsets[3 * (i // 3) + (j // 3)].add(cur)
        return True
