def solution(matrix):
    cost = 0
    countit = [True] * len(matrix[0])
    for floor in matrix:
        for i, price in enumerate(floor):
            if countit[i]:
                if price:
                    cost += price
                else:
                    countit[i] = False
    return cost