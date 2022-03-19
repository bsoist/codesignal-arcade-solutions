def solution(inputArray, elemToReplace, substitutionElem):
    for i, elem in enumerate(inputArray):
        if elem == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray