def solution(upSpeed, downSpeed, desiredHeight):
    day, height = 0, 0
    while True:
        day += 1
        height += upSpeed
        if height >= desiredHeight: return day
        height -= downSpeed