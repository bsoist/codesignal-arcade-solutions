def solution(a):
    bin_str = '0b'
    while a:
        n = a.pop()
        bin_str += format(n, '#010b')[2:]
    return int(bin_str, 2)