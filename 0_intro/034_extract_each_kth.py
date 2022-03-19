def solution(inputArray, k):
    return [n for i, n in 
            enumerate(inputArray)
            if (i+1) % k]
