def solution(matrix):
    grid = []
    height, width = len(matrix), len(matrix[0])
    for row in matrix:
        grid.append([0] * width)
    for i in range(height):
        for j in range(width):
            if not matrix[i][j]: continue
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    x, y = i+a, j+b
                    if x < 0 or y < 0: continue
                    if x == i and y == j: continue
                    try:
                        grid[x][y] += 1
                    except IndexError:
                        continue
    return grid