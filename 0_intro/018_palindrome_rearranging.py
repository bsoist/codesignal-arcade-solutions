from collections import Counter
def solution(inputString):
    values = list(Counter(inputString).values())
    count = len(list(filter(
        lambda n: (n % 2)or (n == 1),
        values
    )))
    return count < 2