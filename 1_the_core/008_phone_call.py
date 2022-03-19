def solution(min1, min2_10, min11, s):
    if min1 > s: return 0
    if min1 == s: return 1
    minutes, s = 1, s - min1
    while minutes < 10:
        if s >= min2_10:
            s -= min2_10
            minutes += 1
        else:
            return minutes
    while s >= min11:
        s -= min11
        minutes += 1
    return minutes