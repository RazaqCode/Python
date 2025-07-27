from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Using defaultdict(set) for convenience
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) # Key will be (row_block, col_block) e.g., (0,0) for top-left 3x3

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue

                # Check row
                if char in rows[r]:
                    return False
                rows[r].add(char)

                # Check column
                if char in cols[c]:
                    return False
                cols[c].add(char)

                # Check 3x3 box
                box_id = (r // 3, c // 3)
                if char in boxes[box_id]:
                    return False
                boxes[box_id].add(char)

        return True

# Test Cases (LeetCode examples or standard valid/invalid boards)
valid_board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(f"Valid Sudoku (valid board): {Solution().isValidSudoku(valid_board)}") # Expected: True

invalid_board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] # Has two 8s in the first column
print(f"Valid Sudoku (invalid board): {Solution().isValidSudoku(invalid_board)}") # Expected: False