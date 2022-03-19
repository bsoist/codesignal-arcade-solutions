def solution(s1, s2):
    count = 0
    s1, s2 = list(s1), list(s2)
    while s1:
        try:
            s2.remove(s1.pop())
        except:
            pass
        else:
            count += 1
    return count