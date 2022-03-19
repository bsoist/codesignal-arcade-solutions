def solution(n):
    while n > 0:
        d = n % 10
        if d % 2: return False
        n = n // 10
    return True
