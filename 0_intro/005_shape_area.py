def solution(n):
    area = 1
    for i in range(1, n):
        area += 4 * i
    return area