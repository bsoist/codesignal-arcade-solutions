def solution(a, b):
    return sum(bin(n).count('1') for n in range(a, b + 1))
       
