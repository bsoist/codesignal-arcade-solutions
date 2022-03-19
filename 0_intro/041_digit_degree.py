def solution(n):
    degree = 0
    while n >= 10:
        degree += 1
        n = sum(map(int, str(n)))
    return degree