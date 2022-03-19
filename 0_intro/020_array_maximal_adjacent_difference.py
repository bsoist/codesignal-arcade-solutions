def solution(inputArray):
    return max(
        [abs(inputArray[i-1] - inputArray[i])
        for i, n in enumerate(inputArray) if i >= 2]
    )
