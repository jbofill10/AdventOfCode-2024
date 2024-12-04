from typing import List


def is_valid(col: int, row: int, col_size: int, row_size: int) -> bool:
    top_left = 0 <= col - 1 < col_size and 0 <= row - 1 < row_size
    top_right = 0 <= col - 1 < col_size and 0 <= row + 1 < row_size

    bottom_left = 0 <= col + 1 < col_size and 0 <= row - 1 < row_size
    bottom_right = 0 <= col + 1 < col_size and 0 <= row + 1 < row_size

    return top_left and top_right and bottom_left and bottom_right


matrix: List[List[str]] = []


def check_for_x_mas(matrix: List[List[str]], col: int, row: int) -> bool:
    left_diag = False
    right_diag = False

    top_left_char = matrix[col - 1][row - 1]
    bottom_right_char = matrix[col + 1][row + 1]

    top_right_char = matrix[col - 1][row + 1]
    bottom_left_char = matrix[col + 1][row - 1]

    if (top_left_char == "M" or top_left_char == "S") and (
        bottom_right_char == "M" or bottom_right_char == "S"
    ):
        left_diag = top_left_char != bottom_right_char

    if (top_right_char == "M" or top_right_char == "S") and (
        bottom_left_char == "M" or bottom_left_char == "S"
    ):
        right_diag = top_right_char != bottom_left_char

    return left_diag and right_diag


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
        if matrix[i][j] == "A" and is_valid(i, j, len(matrix), len(matrix[0])):
            xmas_amount += check_for_x_mas(matrix, i, j)
print(xmas_amount)
