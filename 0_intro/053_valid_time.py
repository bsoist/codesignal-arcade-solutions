def solution(time):
    return (
        (-1 < int(time[:2]) < 24) and
        (-1 < int(time[-2:]) < 60) and
        len(time) == 5
    )