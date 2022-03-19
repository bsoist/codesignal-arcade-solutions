def solution(n):
    digits = []
    while n > 0:
        print(n)
        digits.append(n % 10)
        n = n // 10
    mid = len(digits) // 2
    return sum(digits[:mid]) == sum(digits[mid:])
