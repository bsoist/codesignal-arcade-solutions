def solution(n, m):
    while m % n:
        m -= 1
    return m