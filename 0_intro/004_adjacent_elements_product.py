def solution(inputArray):
    max_product = float('-inf')
    for i in range(1, len(inputArray)):
        max_product = max(max_product, inputArray[i] * inputArray[i-1])
    return max_product