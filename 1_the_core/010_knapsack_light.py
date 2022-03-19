def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    for value, weight in reversed(sorted([(value1, weight1), (value2, weight2)])):
        print(value, weight)
        if weight <= maxW:
            return value
    return 0