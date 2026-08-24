class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)
        for i in range(n // 2):
            for j in range(n):
                mat[i][j], mat[n - i - 1][j] = mat[n - i - 1][j], mat[i][j]
                
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        