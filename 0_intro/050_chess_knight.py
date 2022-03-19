def solution(cell):
    x = ('abcdhgfe'.index(cell[0]) % 4) + 1 or 1
    y = int('012344321'[int(cell[1])])
    print(cell, x, y)
    if 1 in {x, y}: return min(4, x + y)
    if 2 in {x, y}: return min(6, x * y)
    return 8
