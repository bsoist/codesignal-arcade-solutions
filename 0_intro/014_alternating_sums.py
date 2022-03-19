def solution(a):
    weights = [0, 0]
    i = 0
    for weight in a:
        weights[i] += weight
        i = int(not i)
    return weights
