def solution(inputArray, k):
    current_sum = highest_sum = sum(inputArray[:k])
    for i in range(k, len(inputArray)):
        current_sum += inputArray[i] - inputArray[i-k]
        if current_sum > highest_sum:
            highest_sum = current_sum
    return highest_sum

assert solution([1, 3, 2, 4], 3) == 9