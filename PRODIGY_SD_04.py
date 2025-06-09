class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Solved
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  # Backtrack

        return False

    def is_valid(self, num, row, col):
        # Check row
        if num in self.board[row]:
            return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def display(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=" ")
            print()


# Example unsolved Sudoku board (0 means empty)
example_board = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

solver = SudokuSolver(example_board)
if solver.solve():
    print("Solved Sudoku:")
    solver.display()
else:
    print("No solution exists.")