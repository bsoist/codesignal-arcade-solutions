def solution(n, k):
    return int(bin(n)[:-k] + '0' + bin(n)[-k+1:],2) if len(bin(n)) > (k+1) else n