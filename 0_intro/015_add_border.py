def solution(picture):
    bordered = ['*' * (len(picture[0]) + 2)]
    for row in picture:
        bordered.append('*' + row + '*')
    bordered.append(bordered[0])
    return bordered