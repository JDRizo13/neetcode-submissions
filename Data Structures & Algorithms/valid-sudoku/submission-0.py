class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            seen = []
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.append(num)

        # check columns
        for c in range(9):
            seen = []
            for r in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.append(num)

        # check 3x3 boxes
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                seen = []
                for r in range(boxRow, boxRow + 3):
                    for c in range(boxCol, boxCol + 3):
                        num = board[r][c]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.append(num)
        return True