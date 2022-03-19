def solution(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    len_digits = len(digits)
    max_num = 0
    for i in range(len_digits):
        new_digits = digits[:i] + digits[i+1:]
        new_num, place = 0, 1
        for digit in new_digits:
            new_num += digit * place
            place *= 10
        if new_num > max_num:
            max_num = new_num
    return max_num