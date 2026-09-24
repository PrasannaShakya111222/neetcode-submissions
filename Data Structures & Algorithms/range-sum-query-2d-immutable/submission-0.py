class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        self.dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.dp[r + 1][c + 1] = (matrix[r][c] + 
                                         self.dp[r][c + 1] + 
                                         self.dp[r + 1][c] - 
                                         self.dp[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.dp[row2 + 1][col2 + 1] - 
                self.dp[row1][col2 + 1] - 
                self.dp[row2 + 1][col1] + 
                self.dp[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)