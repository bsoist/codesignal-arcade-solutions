def solution(matrix):
    matrices = []
    num_rows, num_cols = len(matrix), len(matrix[0])
    for row in range(num_rows - 1):
        for col in range(num_cols - 1):
            two_by_two = [
                [matrix[row][col], matrix[row][col+1]],
                [matrix[row+1][col], matrix[row+1][col+1]]
            ]
            if two_by_two not in matrices:
                matrices.append(two_by_two)
    return len(matrices)