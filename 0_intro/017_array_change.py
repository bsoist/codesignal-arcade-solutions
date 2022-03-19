def solution(inputArray):
    n = inputArray[0]
    count = 0
    for i in inputArray[1:]:
        if i > n:
            n = i
            continue
        inc = n - i + 1
        count += inc
        n = i + inc
    return count
