class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # square
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not is_valid(
                    board[y_][x_] for x_ in range(x, x + 3) for y_ in range(y, y + 3)
                ):
                    return False

        # columns
        for x in range(9):
            if not is_valid(board[y][x] for y in range(9)):
                return False

        # rows
        for y in range(9):
            if not is_valid(board[y][x] for x in range(9)):
                return False

        return True


def is_valid(arr):
    seen = set()
    for v in arr:
        if v in seen:
            return False
        if v.isdigit():
            seen.add(v)
    return True