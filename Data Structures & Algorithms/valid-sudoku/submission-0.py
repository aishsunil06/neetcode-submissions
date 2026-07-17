class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit == '.':
                    continue
                if digit in rows[row]:
                    return False
                rows[row].add(digit)
                if digit in cols[col]:
                    return False
                cols[col].add(digit)
                box = (row // 3) * 3 + col // 3
                if digit in boxes[box]:
                    return False
                boxes[box].add(digit)
        return True