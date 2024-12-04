from typing import List, Tuple


XMAS_STRING = "XMAS"

directions: List[Tuple[int, int]] = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


def find_xmas(
    matrix: List[List[str]],
    col: int,
    row: int,
    idx: int,
    col_size: int,
    row_size: int,
    direction: Tuple[int, int],
) -> int:

    if matrix[col][row] != XMAS_STRING[idx]:
        return False

    if len(XMAS_STRING) - 1 == idx:
        print(matrix[col][row] + "   " + XMAS_STRING[idx])
        return True
    if 0 <= col + direction[0] < col_size and 0 <= row + direction[1] < row_size:
        if find_xmas(
            matrix,
            col + direction[0],
            row + direction[1],
            idx + 1,
            col_size,
            row_size,
            direction,
        ):
            return 1
    return 0


matrix: List[List[str]] = []

with open("input.txt", "r") as f:
    for row in f.readlines():
        matrix_row = []
        for char in row:
            char = char.strip()
            if char:
                matrix_row.append(char)
        matrix.append(matrix_row)

xmas_amount = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "X":
            for direction in directions:
                xmas_amount += find_xmas(
                    matrix, i, j, 0, len(matrix), len(matrix[0]), direction
                )
print(xmas_amount)
