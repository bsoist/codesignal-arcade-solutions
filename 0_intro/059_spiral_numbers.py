def solution(n):
    steps = n
    indices = [i for i in range(steps)]
    steps -= 1
    mult = 1
    while steps > 0:
        for i in range(steps):
            index = indices[-1] + (n * mult)
            indices.append(index)
        for i in range(steps):
            index = indices[-1] - (1 * mult)
            indices.append(index)
        mult *= -1
        steps -= 1
    matrix = [[0] * n for i in range(n)]
    for i in range(0, n * n):
        x, y = indices[i] // n, indices[i] % n
        matrix[x][y] = i + 1
    #return indices
    return matrix