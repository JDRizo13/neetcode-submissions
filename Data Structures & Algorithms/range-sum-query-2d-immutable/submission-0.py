class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.numMatrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):        
            for c in range(1, cols):
                self.numMatrix[r][c] += self.numMatrix[r][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.numMatrix)
        suma = 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                suma += self.numMatrix[r][col2]
            else:
                suma += (self.numMatrix[r][col2] - self.numMatrix[r][col1 - 1])
        
        return suma
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)