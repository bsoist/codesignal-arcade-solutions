def solution(a):
    min_value = float('inf')
    answer = float('inf')
    for x in a:
        total = 0
        for y in a:
            total += abs(x - y)
            if total >= min_value:
                break
        if total < min_value:
            min_value = total
            answer = x
    return answer