def solution(st):
    def is_pal(s):
        return s == s[::-1]
    if is_pal(st): return st
    len_st = len(st)
    try_len = len_st - 1
    while try_len > 2:
        for i in range(try_len):
            if is_pal(st[i:]):
                return st + st[:i][::-1]
        try_len -= 1
    return st + st[:-1][::-1]




'''
    len_st = len(st)
    mid = len_st // 2
    s, e = mid - 1, mid
    pal = {'len': 0, 'pivot': mid}
    
    def longest_pal(pivot, odd):
        while st[s] == st[e]:
            pass

    if len_st % 2: e += 1
        pal['len'] += 1
'''